from enum import Enum


class GameState(Enum):
    Running = 1
    Failed = 2
    Won = 3


class Action:
    def __init__(self, value):
        self.value = value


class ActionSpace:
    MoveLeft = Action(-1)
    MoveUp = Action(-3)
    MoveDown = Action(3)
    MoveRight = Action(1)


class State:
    def __init__(self, numList, emptyPos):
        self.numList = numList
        self.emptyPos = emptyPos

    def __str__(self):
        new = [
            *self.numList[0 : self.emptyPos],
            " ",
            *self.numList[self.emptyPos : len(self.numList) + 1],
        ]
        print(new)

        temp = ""
        for i in range(0, len(new)):
            temp += str(new[i])
            if (i + 1) % 3 == 0:
                temp += "\n"

        return temp
        # return f"{self.numList[0:self.emptyPos]}{self.numList[self.emptyPos+1:len(self.numList)]}"


class Game:
    gameStatus: GameState = GameState.Running
    movePerformed: Action = None
    goalState: State = State([1, 2, 3, 4, 5, 6, 7, 8], 8)

    def __init__(self, gameState: State):
        self.gameState = gameState

    def __str__(self):
        # temp = f"Current State:\n{self.gameState}\nGoal State:\n{self.goalState}"
        temp = f"Current State:\n{self.gameState}"
        return temp

    def move(self, action: Action):
        if self.gameStatus != GameState.Running:
            return False

        if action == ActionSpace.MoveLeft:
            if (self.gameState.emptyPos + 1) % 3 == 1:
                return False

        if action == ActionSpace.MoveUp:
            if self.gameState.emptyPos < 3:
                return False

        if action == ActionSpace.MoveDown:
            if self.gameState.emptyPos > 5:
                return False

        if action == ActionSpace.MoveRight:
            if (self.gameState.emptyPos + 1) % 3 == 0:
                return False

        self.gameState.emptyPos += action.value
        return True


a = Game(State([2, 8, 3, 1, 6, 4, 7, 5], 7))
a.move(ActionSpace.MoveUp)
print(a)
