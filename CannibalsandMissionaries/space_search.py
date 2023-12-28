from CannibalsandMissionaries.game import GameState, ActionSpace, Game
import copy


class Node:
    def __init__(self, state: Game):
        self.data = state
        self.parent = []
        self.children = []
        self.terminated = False
        self.goal = False

    def __eq__(self, other):
        if isinstance(other, Node):
            if (
                self.data.gameState.missionaries == other.data.gameState.missionaries
                and self.data.gameState.cannibals == other.data.gameState.cannibals
                and self.data.gameState.cannoe == other.data.gameState.cannoe
            ):
                return True
            else:
                return False

        return False

    def __str__(self):
        return f"Node: {self.data}, Goal: {self.goal}, Terminated: {self.terminated}, Last Move Performed: {self.data.movePerformed}"

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_all_children(self):
        child_list = []

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.Missionary)

        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.Cannibal)

        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.TwoMissionaries)

        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.TwoCannibals)

        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MissionaryCannibal)

        if can_move:
            node = Node(game)
            child_list.append(node)

        return child_list


class Search:
    def __init__(self, root: Node = Node(state=Game())):
        self.root = root
        self.finished = False
        self.searchedNodes = []
        self.graphvizzes = ['digraph {']

    def start_search_bfs(self):
        queue = []
        queue.append(self.root)
        # initial_node = self.root
        # children = initial_node.get_all_children()
        # for child in children:
        #     child.parent.append(initial_node)
        #     initial_node.add_child(child)

        # self.searchedNodes.append(initial_node)

        # queue.append(children)
        answers = []
        while queue:
            current_node = queue.pop(0)

            if current_node in self.searchedNodes:
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                current_node.terminated = True
                self.finished = True
                answers.append(current_node)
                continue

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in current_node.parent:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        if child not in self.searchedNodes:
                            queue.append(child)
                            if child.data.gameStatus == GameState.Won:
                                child.terminated = True
                                child.goal = True
                                self.finished = True
                                answers.append(child)
        return answers

    def start_single_search_bfs(self):
        print("BFS ...")
        generatedNodes = set()
        generatedNodes.add(str(self.root.data.gameState))
        queue = []
        queue.append(self.root)
        self.graphvizzes.append(f'"{self.root.data.gameState.missionaries}, {self.root.data.gameState.cannibals}, {self.root.data.gameState.cannoe}" [style=filled, color=lightblue]}}')
        count = 0
        while queue:
            current_node = queue.pop(0)
            if current_node in self.searchedNodes:
                continue

            count += 1
            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    print(f"Checker : {str(child.data.gameState)} and {generatedNodes} and {str(child.data.gameState) not in generatedNodes}")
                    if str(child.data.gameState) not in generatedNodes:
                        generatedNodes.add(str(child.data.gameState))
                        self.graphvizzes.append(f'"{current_node.data.gameState.missionaries}, {current_node.data.gameState.cannibals}, {current_node.data.gameState.cannoe}" -> "{child.data.gameState.missionaries}, {child.data.gameState.cannibals}, {child.data.gameState.cannoe}" [label="{child.data.movePerformed}"]}}')
                       
                        queue.append(child)
                        if child.data.gameStatus == GameState.Won:
                            self.graphvizzes.append(f'"{child.data.gameState.missionaries}, {child.data.gameState.cannibals}, {child.data.gameState.cannoe}" [style=filled, color=lightgreen]}}')
                            self.finished = True
                            print(f"Total No of States: {count}")
                            return child
                        
    # def start_single_search_bfs(self):
    #     queue = []
    #     queue.append(self.root)

    #     while queue:
    #         current_node = queue.pop(0)
    #         if current_node in self.searchedNodes:
    #             current_node.terminated = True
    #             continue

    #         self.searchedNodes.append(current_node)

    #         if current_node.data.gameStatus == GameState.Won:
    #             current_node.root.goal = True
    #             self.finished = True
    #             return current_node

    #         if current_node.data.gameStatus == GameState.Running:
    #             children = current_node.get_all_children()
    #             for child in children:
    #                 if child not in self.searchedNodes:
    #                     child.parent.append(current_node)
    #                     current_node.add_child(child)
    #                     queue.append(child)
    #                     if child.data.gameStatus == GameState.Won:
    #                         child.goal = True
    #                         self.finished = True
    #                         return child

    def start_search_dfs(self):
        stack = []
        stack.append(self.root)

        answers = []

        while stack:
            current_node = stack.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                current_node.terminated = True
                self.finished = True
                answers.append(current_node)
                continue

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                temp = []
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        temp.append(child)
                        if child.data.gameStatus == GameState.Won:
                            child.goal = True
                            child.terminated = True
                            self.finished = True
                            answers.append(child)

                stack = [*temp, *stack]

        return answers

    def start_single_search_dfs(self):
        stack = []
        stack.append(self.root)

        while stack:
            current_node = stack.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                current_node.root.goal = True
                self.finished = True
                return current_node

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                temp = []
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        temp.append(child)
                        if child.data.gameStatus == GameState.Won:
                            child.goal = True
                            self.finished = True
                            return child

                stack = [*temp, *stack]


    def start_single_search_dfs(self):
        print("DFS ...")
        generatedNodes = set()
        generatedNodes.add(str(self.root.data.gameState))
        stack = []
        stack.append(self.root)
        self.graphvizzes.append(f'"{self.root.data.gameState.missionaries}, {self.root.data.gameState.cannibals}, {self.root.data.gameState.cannoe}" [style=filled, color=lightblue]}}')

        count = 0
        while stack:
            current_node = stack.pop(0)
            if current_node in self.searchedNodes:
                continue
            
            count += 1
            self.searchedNodes.append(current_node)

            # if current_node.data.gameStatus == GameState.Won:
            #     self.finished = True
            #     print(f"Total No of States: {count}")
            #     return current_node
            if (count % 100 == 0):
                print(f"No of States Generated: {count}")

            # if current_node.data.gameStatus == GameState.Running and current_depth <= 3:
            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                temp = []
                for child in children:
                    if str(child.data.gameState) not in generatedNodes:
                        generatedNodes.add(str(child.data.gameState))
                        self.graphvizzes.append(f'"{current_node.data.gameState.missionaries}, {current_node.data.gameState.cannibals}, {current_node.data.gameState.cannoe}" -> "{child.data.gameState.missionaries}, {child.data.gameState.cannibals}, {child.data.gameState.cannoe}" [label="{child.data.movePerformed}"]}}')
                        
                        # temp.append({"node" :child, "depth": current_depth + 1})
                        temp.append(child)
                        if child.data.gameStatus == GameState.Won:
                            self.graphvizzes.append(f'"{child.data.gameState.missionaries}, {child.data.gameState.cannibals}, {child.data.gameState.cannoe}" [style=filled, color=lightgreen]}}')

                            self.finished = True
                            print(f"Total No of States: {count}")
                            return child
                        
                stack = [*temp, *stack]
