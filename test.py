# Unit Testing Code

import sys
from tictactoe import tictactoe


class TestCases(tictactoe):

    def __init__(self):
        print '\n\n'
        print 'Initialised Unit Testing for TicTacToe.'
        print '-' * 50

    def testPassAllValues(self):

        print '1: Testing Register Moves for all possible values.'
        for i in range(0, 3):
            for j in range(0, 3):
                print 'Testing registerMove(' + str(i) + ', ' + str(j) + ')'
                game = tictactoe()
                try:
                    assert game.registerMove(i, j) == True
                except AssertionError as e:
                    print '-' * 50
                    print 'Test Cases Failed'
                    print '\n\n'
                    return e

        print '-' * 50
        print '9 Values checked ...'
        print 'Test Case passed.'
        print '\n\n'
        return True

    def testWinCases(self):
        print '2: Testing Winning returns for all win types possible.'

        game = tictactoe()
        agent = []
        # Making all possible column wins
        for k in range(1, 3):
            for i in range(0, 3):
                agent.append([])

if __name__ == '__main__':
    # game = tictactoe()
    test = TestCases()
    test.testPassAllValues()
