
import numpy as np
import sys


class tictactoe(object):

    def __init__(self):
        self.agent = []
        for i in range(0, 3):
            self.agent.append([0, 0, 0])

    def displayBoard(self):
        print "Game Board"
        for i in range(0, 3):
            print '\t',
            for j in range(0, 3):
                if self.agent[i][j] == 0:
                    sys.stdout.write('-')
                elif self.agent[i][j] == 1:
                    sys.stdout.write('X')
                elif self.agent[i][j] == 2:
                    sys.stdout.write('O')
                if j < 2:
                    sys.stdout.write('|')
            print

    def registerMove(self, x, y):
        self.agent[x][y] = 2
        if self.gameWin():
            return False

    def gameWin(self):
        for i in range(0, 3):
            # Checking Rows
            if (self.agent[i][0] == self.agent[i][1] and self.agent[i][0] == self.agent[i][2]):
                if self.agent[i][0] == 2:
                    print "O wins"
                if self.agent[i][0] == 1:
                    print "X wins"
                return True

            # Checking Columns
            if (self.agent[0][i] == self.agent[1][i] and self.agent[0][i] == self.agent[2][i]):
                if self.agent[0][i] == 2:
                    print "O wins"
                if self.agent[0][i] == 1:
                    print "X wins"
                return True

        # Checking Diagonals
        if (self.agent[0][0] == self.agent[1][1] and self.agent[0][0] == self.agent[1][1]) or \
                (self.agent[0][2] == self.agent[1][1] and self.agent[0][2] == self.agent[2][0]):
            if self.agent[1][1] == 2:
                print "O wins"
            elif self.agent[1][1] == 1:
                print "X wins"
            return True


if __name__ == '__main__':
    game = tictactoe()
    game.displayBoard()
    game.registerMove(1, 1)
    game.displayBoard()
