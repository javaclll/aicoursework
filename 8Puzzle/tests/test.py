import sys
import unittest

sys.path.append("../")
from game import State, Action, ActionSpace, Game
from space_search import Node, Search


class TestSearch(unittest.TestCase):
    def testIntegratedGame(self):
        searching = Search(
            Node(
                Game(
                    State([2, 4, 6, 7, 3, 1, " ", 5, 8]),
                    State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
        temp = searching.start_single_search_bfs()

        while len(temp.parent) != 0:
            print(temp)
            temp = temp.parent[0]

        print(searching.root)
        self.assertEqual(searching.finished, True)


if __name__ == "__main__":
    unittest.main()
