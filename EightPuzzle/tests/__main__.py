import unittest

from EightPuzzle.game import State, Action, ActionSpace, Game
from EightPuzzle.space_search import Node, Search, Heuristics


class TestSearch(unittest.TestCase):
    def testIntegratedGame(self):
        searching = Search(
            Node(
                Game(
                    State([1, " ", 2, 3, 4, 5, 6, 7, 8]),
                    State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
       
        depth = 2
        # temp = searching.start_search_idfs(depth)
        # temp = searching.start_search_misplaced()
        temp = searching.start_search_manhatten()
        if(temp is None):
            print(f"Cannot find the end state within {depth} depth.")
        else:
            while len(temp.parent) != 0:
                print(temp)
                temp = temp.parent[0]

            print(f"root: {searching.root}")
            print(searching.finished)
            self.assertEqual(searching.finished, True)


if __name__ == "__main__":
    unittest.main()
