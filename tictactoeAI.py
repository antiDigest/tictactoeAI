
import numpy as np
import sys
from tictactoe import tictactoe

import random
import re


class tictactoeAI(tictactoe):

    def __init__(self):
        pass

    def makeMove(self, game):

        if game.end == 1:
            del game
            del self
            print "END OF GAME"
            return False

        for i in range(0, 3):
            for j in range(0, 3):
                if game.agent[i][j] == 0:
                    game.agent[i][j] = 1
                    break
            break

        return self.gameWin()

    def makeRandomMove(self, game):

        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if game.agent[i][j] == 0 and game.end == 0:
            game.agent[i][j] = 1
            return game.gameWin()
        elif game.end == 0:
            self.makeRandomMove(game)
            return game.gameWin()
        else:
            del game
            del self
            print "END OF GAME"
            return False


if __name__ == '__main__':
    game = tictactoe()
    ai = tictactoeAI()

    # Moves
    while(1):
        game.displayBoard()

        try:
            string = raw_input('Enter you move: ')
            i, j = int(re.split(',[ ]*', string)[0]
                       ), int(re.split(',[ ]*', string)[1])
            if i > 2 or j > 2:
                print "Values of x and y should be less than 2"
                continue
        except ValueError:
            print 'Please keep the format of entry: x,y'
            continue

        if not game.registerMove(i, j):
            break
        if not ai.makeRandomMove(game):
            break
