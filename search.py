from collections import deque
from game import GameState, State, Action, ActionSpace, Game
import copy


class SearchTree:
    def __init__(self, nodeState: Game):
        self.data = nodeState
        self.children = []
        self.terminate = False
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_all_states(self):
        stateList = []

        temp_game = copy.deepcopy(self.data)
        can_move = temp_game.move(ActionSpace.Missionary)
        if can_move:
            temp_node = SearchTree(temp_game)
            stateList.append(temp_node)

        temp_game = copy.deepcopy(self.data)
        can_move = temp_game.move(ActionSpace.Cannibal)
        if can_move:
            temp_node = SearchTree(temp_game)
            stateList.append(temp_node)

        temp_game = copy.deepcopy(self.data)
        can_move = temp_game.move(ActionSpace.TwoMissionaries)
        if can_move:
            temp_node = SearchTree(temp_game)
            stateList.append(temp_node)

        temp_game = copy.deepcopy(self.data)
        can_move = temp_game.move(ActionSpace.TwoCannibals)
        if can_move:
            temp_node = SearchTree(temp_game)
            stateList.append(temp_node)

        temp_game = copy.deepcopy(self.data)
        can_move = temp_game.move(ActionSpace.MissionaryCannibal)
        if can_move:
            temp_node = SearchTree(temp_game)
            stateList.append(temp_node)
        return stateList

    def __eq__(self, other):
        if isinstance(other, SearchTree):
            if (
                self.data.gameState.missionaries == other.data.gameState.missionaries
                and self.data.gameState.cannibals == other.data.gameState.cannibals
                and self.data.gameState.cannoe == other.data.gameState.cannoe
            ):
                return True
            else:
                return False

        return False

    def searchState():
        queue = []
        visited = []
        newGame = Game()
        initialNode = SearchTree(newGame)
        children = initialNode.get_all_states()
        queue.extend(children)
        visited.append(initialNode)
        for child in children:
            initialNode.add_child(child)

        while queue:
            current_state = queue.pop(0)
            if current_state in visited:
                continue
            visited.append(current_state)
            if current_state.data.gameStatus == GameState.Won:
                # print(f"Success: {current_state.data}")
                break
            if current_state.data.gameStatus == GameState.Running:
                new_states = current_state.get_all_states()
                for new_state in new_states:
                    if new_state not in visited:
                        queue.append(new_state)

    def searchState2():
        queue = []
        visited = []
        newGame = Game()
        initialNode = SearchTree(newGame)
        queue.append(initialNode)
        while queue:
            current_state = queue.pop(0)
            if current_state in visited:
                continue
            visited.append(current_state)
            if current_state.data.gameStatus == GameState.Won:
                # print(f"Success: {current_state.data}")
                return current_state

            if current_state.data.gameStatus == GameState.Running:
                new_states = current_state.get_all_states()
                for new_state in new_states:
                    current_state.add_child(new_state)
                    new_state.parent = current_state
                    if new_state not in visited:
                        queue.append(new_state)

    # def __repr__(self, level=0):
    #     ret = "\t" * level + repr(self.data) + "\n"
    #     for child in self.children:
    #         ret += child.__repr__(level + 1)
    #     return ret

    def __str__(self):
        return f"{self.data}"


# # Create nodes
# root = SearchTree("Root")
# child1 = SearchTree("Child 1")
# child2 = SearchTree("Child 2")
# child3 = SearchTree("Child 3")
# root.add_child(child1)
# root.add_child(child2)
# child1.add_child(child3)

# # Perform breadth-first traversal and print the result
# result = root.breadth_first_traversal()
# print(result)
game = Game()
searchTreeResult = SearchTree.searchState2()

temp = searchTreeResult
while temp != None:
    print(temp)
    temp = temp.parent
