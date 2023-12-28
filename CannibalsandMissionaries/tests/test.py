import sys
import unittest

sys.path.append("../")
from game import State, Action, ActionSpace, Game
from space_search import Node, Search


class TestGame(unittest.TestCase):
    def testIntegratedGame(self):
        searching = Search()
        temp = searching.start_search_dfs()

        for t in temp:
            while len(t.parent) != 0:
                print(t)
                t = t.parent[0]
            print("\n")

        self.assertEqual(searching.finished, True)


if __name__ == "__main__":
    unittest.main()
