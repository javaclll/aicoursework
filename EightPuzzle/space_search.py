from .game import GameState, ActionSpace, Game, State
import bisect

import copy
import math

class Heuristics:
    @staticmethod
    def manhatten_distance(node):
        manhatten = 0
        for k in range(1,9):
            actual_index = node.data.gameState.numList.index(k)
            i = math.floor(actual_index/3)
            j = actual_index - 3 * i

            goal_index = node.data.goalState.numList.index(k)
            encoded_i = math.floor(goal_index/3)
            encoded_j = goal_index - 3 * encoded_i

            manhatten = manhatten + abs(encoded_i- i) + abs(encoded_j - j)

        index = node.data.gameState.numList.index(" ")
        i = math.floor(index/3)
        j = index - 3 * i
        
        goal_index = node.data.goalState.numList.index(" ")
        encoded_i = math.floor(goal_index/3)
        encoded_j = goal_index - 3 * encoded_i

        return manhatten + abs(encoded_i- i) + abs(encoded_j - j)

    @staticmethod
    def no_of_misplaced_tiles(node):
        misplaced = 0
        for i in range(1, 9):
            if node.data.gameState.numList.index(i) != node.data.goalState.numList.index(i):
                misplaced += 1
        
        if node.data.gameState.numList.index(" ") != node.data.goalState.numList.index(" "):
            misplaced += 1 

        return misplaced
    
class Node:
    def __init__(self, state: Game):
        self.data = state
        self.parent = []
        self.children = []
        self.terminated = False
        self.goal = False
        self.f_value = math.inf
        self.g_value = math.inf

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
        self.graphvizzes = ['digraph {']

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
        count = 0
        while queue:
            current_node = queue.pop(0)
            print(count)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue
            count += 1
            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                self.finished = True
                return current_node

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in self.searchedNodes:
                        self.graphvizzes.append(f'"{str(current_node.data.gameState)}" -> "{str(child.data.gameState)}" [label="{child.data.movePerformed}"]}} ')
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        queue.append(child)
                        if child.data.gameStatus == GameState.Won:
                            self.finished = True
                            return child
                        
                        

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

    def start_search_idfs(self, max_depth):
        for depth in range(max_depth + 1):
            result = self.depth_limited_search(self.root, depth)
            if result is not None:
                return result
    
    def depth_limited_search(self, node, depth):
        if depth == 0:
            if node.data.gameStatus == GameState.Won:
                self.finished = True
                return node
            return None

        if node in self.searchedNodes:
            node.terminated = True

        self.searchedNodes.append(node)

        if node.data.gameStatus == GameState.Running:
            children = node.get_all_children()
            for child in children:
                if child not in self.searchedNodes:
                    child.parent.append(node)
                    node.add_child(child)
                    result = self.depth_limited_search(child, depth=depth - 1)
                    if result is not None:
                        return result        

    def start_search_manhatten(self):
        self.root.g_value = 0
        self.root.f_value = Heuristics.manhatten_distance(self.root)
        list = []
        list.append(self.root)

        node_count = 0
        while list:
            node_count += 1
            current_node = list.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                self.finished = True
                print(f"Nodes Expanded: {node_count}")
                return current_node

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        child.g_value = current_node.g_value + 1
                        child.f_value = Heuristics.manhatten_distance(child) + child.g_value
                        bisect.insort(list, child, key= lambda x: x.f_value)
        
        
    def start_search_misplaced(self):
        self.root.g_value = 0
        self.root.f_value = Heuristics.no_of_misplaced_tiles(self.root)
        list = []
        list.append(self.root)
        node_count = 0
        while list:
            node_count += 1
            current_node = list.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                self.finished = True
                print(f"Nodes Expanded: {node_count}")
                return current_node

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        child.g_value = current_node.g_value + 1
                        child.f_value = Heuristics.no_of_misplaced_tiles(child) + child.g_value
                        bisect.insort(list, child, key= lambda x: x.f_value)

