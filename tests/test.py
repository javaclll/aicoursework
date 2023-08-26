import sys
import unittest

sys.path.append("../")
from game import State, Action, ActionSpace, Game


class TestGame(unittest.TestCase):
    def testIntegratedGame(self):
        newGame = Game()
        actions = [
            ActionSpace.TwoCannibals,
            ActionSpace.Cannibal,
            ActionSpace.TwoCannibals,
            ActionSpace.Cannibal,
            ActionSpace.TwoMissionaries,
            ActionSpace.MissionaryCannibal,
            ActionSpace.TwoMissionaries,
            ActionSpace.Cannibal,
            ActionSpace.TwoCannibals,
            ActionSpace.Cannibal,
            ActionSpace.TwoCannibals,
        ]
        for action in actions:
            newGame.move(action)

        goalState = State(0, 0, False)

        result = newGame.gameState
        self.assertEqual(result.missionaries, goalState.missionaries)
        self.assertEqual(result.cannibals, goalState.cannibals)
        self.assertEqual(result.cannoe, goalState.cannoe)


if __name__ == "__main__":
    unittest.main()
