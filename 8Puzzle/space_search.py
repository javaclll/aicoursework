from game import GameState, ActionSpace, Game, State
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
            if self.data.gameState.numList == other.data.gameState.numList:
                return True
            else:
                return False

        return False

    def __str__(self):
        return f"Move Performed: {self.data.movePerformed} Node:\n{self.data}"

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_all_children(self):
        child_list = []

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveLeft)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveUp)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveDown)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveRight)
        if can_move:
            node = Node(game)
            child_list.append(node)
        return child_list


class Search:
    def __init__(self, root: Node):
        self.root = root
        self.finished = False
        self.searchedNodes = []

    def start_search_bfs(self):
        queue = []
        queue.append(self.root)

        while queue:
            current_node = queue.pop(0)

            if current_node in self.searchedNodes:
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                continue

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in current_node.parent:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        if child not in self.searchedNodes:
                            queue.append(child)

    def start_single_search_bfs(self):
        queue = []
        queue.append(self.root)

        while queue:
            current_node = queue.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                self.finished = True
                return current_node

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        queue.append(child)

    def start_search_dfs(self):
        stack = []
        stack.append(self.root)

        while stack:
            current_node = stack.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                continue

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                temp = []
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        temp.append(child)

                stack = [*temp, *stack]

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

                stack = [*temp, *stack]
