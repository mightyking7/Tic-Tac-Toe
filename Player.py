from Game import Board
import random

class Player:

    # Player has a name and an assigned piece to make moves
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    def makeMove(self, square):

        # select randomly available square
        square = random.randint(Board.getAvailableSquares())

        Board.markSquare(square, self.letter)


