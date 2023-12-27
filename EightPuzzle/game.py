from enum import Enum


class GameState(Enum):
    Running = 1
    Won = 3


class Action:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self == ActionSpace.MoveLeft:
            return "Left"
        elif self == ActionSpace.MoveUp:
            return "Up"
        elif self == ActionSpace.MoveDown:
            return "Down"
        elif self == ActionSpace.MoveRight:
            return "Right"
        else:
            return "Unknown Action"


class ActionSpace:
    MoveLeft = Action(-1)
    MoveUp = Action(-3)
    MoveDown = Action(3)
    MoveRight = Action(1)


class State:
    def __init__(self, numList):
        self.numList = numList

    def __str__(self):
        temp = ""
        for i in range(0, len(self.numList)):
            if(self.numList[i] == " "):
                temp += str("-")
            else:
                temp += str(self.numList[i])
            if (i + 1) % 3 == 0:
                temp += "\n"
        return temp


class Game:
    gameStatus: GameState = GameState.Running
    movePerformed: Action = None

    def __init__(self, gameState: State, goalState: State):
        self.gameState = gameState
        self.goalState = goalState

    def __str__(self):
        # temp = f"Current State:\n{self.gameState}\nGoal State:\n{self.goalState}"
        temp = f"Current State:\n{self.gameState}"
        return temp

    def check_game(self):
        if self.gameState.numList == self.goalState.numList:
            self.gameStatus = GameState.Won

    def move(self, action: Action):
        emptyPos = self.gameState.numList.index(" ")
        if self.gameStatus != GameState.Running:
            return False

        if action == ActionSpace.MoveLeft:
            if (emptyPos + 1) % 3 == 1:
                return False

        if action == ActionSpace.MoveUp:
            if emptyPos < 3:
                return False

        if action == ActionSpace.MoveDown:
            if emptyPos > 5:
                return False

        if action == ActionSpace.MoveRight:
            if (emptyPos + 1) % 3 == 0:
                return False

        self.gameState.numList[emptyPos] = self.gameState.numList[
            emptyPos + action.value
        ]
        self.gameState.numList[emptyPos + action.value] = " "
        self.movePerformed = action
        self.check_game()
        return True
