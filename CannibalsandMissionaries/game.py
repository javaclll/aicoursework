from enum import Enum


class GameState(Enum):
    Running = 1
    Failed = 2
    Won = 3


class Action:
    def __init__(self, missionaries, cannibals):
        self.missionaries = missionaries
        self.cannibals = cannibals

    def __str__(self):
        if self == ActionSpace.Cannibal:
            return "(0,1)"
        elif self == ActionSpace.Missionary:
            return "(1,0)"
        elif self == ActionSpace.MissionaryCannibal:
            return "(1,1)"
        elif self == ActionSpace.TwoMissionaries:
            return "(2,0)"
        elif self == ActionSpace.TwoCannibals:
            return "(0,2)"
        else:
            return "Unknown Action"


class ActionSpace:
    Cannibal = Action(0, 1)
    Missionary = Action(1, 0)
    MissionaryCannibal = Action(1, 1)
    TwoMissionaries = Action(2, 0)
    TwoCannibals = Action(0, 2)


class State:
    def __init__(self, missionaries, cannibals, canoe):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.cannoe = canoe

    def __str__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Cannoe: {self.cannoe}"


class Game:
    gameStatus: GameState = GameState.Running
    movePerformed: ActionSpace = None

    def __init__(self):
        self.gameState = State(3, 3, True)

    def check_game(self):
        otherSide = State(
            3 - self.gameState.missionaries,
            3 - self.gameState.cannibals,
            not self.gameState.cannoe,
        )

        if (
            self.gameState.cannibals > self.gameState.missionaries
            and self.gameState.missionaries != 0
        ) or (
            otherSide.cannibals > otherSide.missionaries and otherSide.missionaries != 0
        ):
            self.gameStatus = GameState.Failed
            return

        if self.gameState.missionaries < 0 or self.gameState.cannibals < 0:
            self.gameStatus = GameState.Failed
            return

        if self.gameState.missionaries > 3 or self.gameState.cannibals > 3:
            self.gameStatus = GameState.Failed
            return

        if (
            self.gameState.missionaries == 0
            and self.gameState.cannibals == 0
            and self.gameState.cannoe == False
        ):
            self.gameStatus = GameState.Won
            return

        self.gameStatus = GameState.Running

    def move(self, action):
        next_state = State(
            self.gameState.missionaries, self.gameState.cannibals, self.gameState.cannoe
        )
        if self.gameStatus != GameState.Running:
            return False

        if self.gameState.cannoe:
            next_state.missionaries -= action.missionaries
            next_state.cannibals -= action.cannibals
        else:
            next_state.missionaries += action.missionaries
            next_state.cannibals += action.cannibals

        next_state.cannoe = not self.gameState.cannoe

        if (
            next_state.missionaries < 0
            or next_state.missionaries > 3
            or next_state.cannibals < 0
            or next_state.cannibals > 3
        ):
            self.gameStatus = GameState.Failed
            return False

        self.movePerformed = action
        self.gameState = next_state
        # print(next_state)
        self.check_game()
        return True

    # def __str__(self):
    #     return f"Missionaries: {self.gameState.missionaries}, Cannibals: {self.gameState.cannibals}, Cannoe: {self.gameState.cannoe}, Game check: {self.gameStatus}"

    def __str__(self):
        return f"({self.gameState.missionaries}, {self.gameState.cannibals}, { 0 if(self.gameState.cannoe) else 1})"
