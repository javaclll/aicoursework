from collections import deque
from game import GameState, State, Action, ActionSpace, Game
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
        return f"Node: {self.data}, Goal: {self.goal}, Terminated: {self.terminated}"
    
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
    def __init__(self, root: Node = Node(state = Game())):
        self.root = root
        self.finished = False
        self.searchedNodes = []

    def start_search(self):
        queue = []
        queue.append(self.root)
        # initial_node = self.root
        # children = initial_node.get_all_children()
        # for child in children:
        #     child.parent.append(initial_node)
        #     initial_node.add_child(child)
        
        # self.searchedNodes.append(initial_node)

        # queue.append(children) 

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

    def start_single_search(self):
        queue = []
        queue.append(self.root)

        while queue:
            current_node = queue.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue
        
            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                break

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        queue.append(child)
                
