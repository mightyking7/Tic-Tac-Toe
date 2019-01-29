
from Board import *

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

    # responsible for printing the contents of the board
    def printBoard(self):

        # index for slicing
        i = 0
        j = 3

        while j <= len(self.board.squares):

            row = self.board.squares[i:j]
            print('%c|%c|%c' %(row[0], row[1], row[2]))
            i = j
            j += 3

