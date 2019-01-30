
import random

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
        self.players = []

    '''
        Responsible for printing the contents of the board
    '''
    def printBoard(self):

        # index for slicing
        i = 0
        j = 3

        while j <= len(self.board.squares):

            row = self.board.squares[i:j]
            print('%c|%c|%c' %(row[0], row[1], row[2]))
            i = j
            j += 3
    '''
        Starts a new match
    '''
    def startMatch(self):

        self.currentPlayer = self.players[0]


        square = self.promptPlayerMove()

        self.currentPlayer.makeMove()


    '''
        Used to add a player to the game
        
        player - Player object to add to the game
    '''
    def addPlayer(self, player):

        self.players.append(player)


class Player:

    # Player has a name and an assigned piece to make moves
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    def makeMove(self, board, square):

        # select randomly available square
        square = random.randint(Board.getAvailableSquares())

        board.markSquare(square, self.letter)


'''
    Responsible for maintaining the
    states of individual squares in the board

    Isaac Buitrago
'''
class Board:

    def __init__(self):
        self.squares = [ ' ' for i in range(9)]


