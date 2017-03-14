
import numpy as np
import sys


class tictactoe(object):

    def __init__(self):
        self.agent = []
        self.end = 0
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
        if self.agent[x][y] == 0 and self.end == 0:
            self.agent[x][y] = 2
            return self.gameWin()
        elif self.end == 0:
            print('Not a valid move !')
            return "Invalid Move"
        else:
            del self
            print "END OF GAME"
            return False

    def gameWin(self):

        # Checking rows
        for i in range(0, 3):
            # O Wins
            if (self.agent[i][0] == 1 and self.agent[i][2] == 1 and self.agent[i][1] == 1):
                print "X wins"
                self.displayBoard()
                self.end = 1
                return False
            # Does X win ?
            if (self.agent[i][0] == 2 and self.agent[i][2] == 2 and self.agent[i][1] == 2):
                print "O wins"
                self.displayBoard()
                self.end = 1
                return False

        # Checking Columns
        for i in range(0, 3):
            # Does O win ?
            if (self.agent[0][i] == 1 and self.agent[2][i] == 1 and self.agent[1][i] == 1):
                print "X wins"
                self.displayBoard()
                self.end = 1
                return False
            # Does X win ?
            if (self.agent[0][i] == 2 and self.agent[2][i] == 2 and self.agent[1][i] == 2):
                print "O wins"
                self.displayBoard()
                self.end = 1
                return False

        # Checking Diagonals
        for k in range(1, 3):
            if (self.agent[0][0] == k and self.agent[1][1] == k and self.agent[2][2] == k):
                if k == 2:
                    print "O wins"
                    self.displayBoard()
                    self.end = 1
                    return False
                else:
                    print "X wins"
                    self.displayBoard()
                    self.end = 1
                    return False

        for k in range(1, 3):
            if (self.agent[0][2] == k and self.agent[1][1] == k and self.agent[2][0] == k):
                if k == 2:
                    print "O wins"
                    self.displayBoard()
                    self.end = 1
                    return False
                else:
                    print "X wins"
                    self.displayBoard()
                    self.end = 1
                    return False

        return True


if __name__ == '__main__':
    game = tictactoe()
    game.displayBoard()
    game.registerMove(1, 1)
    game.displayBoard()
