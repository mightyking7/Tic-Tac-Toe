
import Board

'''
    Responsible for controlling state of game
    and determining the winner of a match

    Isaac Buitrago
'''
class Game:

    def __init__(self):
        self.board = Board()
        self.currentPlayer = None
        self.winner = None

    def printBoard(self):

        # index for slicing
        j = 0
        i = 3

        for row in self.board.squares[j:i]:
            print('%c|%c|%c' %(row[0], row[1], row[2]))
            j = i
            i += 3

