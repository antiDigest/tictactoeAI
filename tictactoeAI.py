
import numpy as np
import sys
from tictactoe import tictactoe


class tictactoeAI(object):

    def __init__(self):
        pass

    def makeMove(self, game):

        for i in range(0, 3):
            for j in range(0, 3):
                if game.agent[i][j] == 0:
                    game.agent[i][j] = 1
                    break
            break
        if game.gameWin():
            return False


if __name__ == '__main__':
    game = tictactoe()
    ai = tictactoeAI()
    game.displayBoard()
    # Move 1
    game.registerMove(0, 1)
    ai.makeMove(game)
    game.displayBoard()
    # Move 2
    game.registerMove(0, 2)
    ai.makeMove(game)
    game.displayBoard()
    # Move 3
    game.registerMove(1, 2)
    ai.makeMove(game)
    game.displayBoard()
    # Move 4
    game.registerMove(2, 0)
    ai.makeMove(game)
    game.displayBoard()
    # Move 5
    game.registerMove(2, 0)
    ai.makeMove(game)
    game.displayBoard()
    # Move 6 - AI will not be able to make any move now.
    game.registerMove(2, 2)
    ai.makeMove(game)
    game.displayBoard()
