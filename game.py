
import re
from exceptions import TakenSquareException

'''
    Responsible for controlling state of game
    and determining the winner of a match

    Isaac Buitrago 
'''
class Game():

    # constructor for game
    def __init__(self):
        self.board = Board()
        self.currentPlayer = None
        self.players = []

    '''
        Starts a new match
    '''
    def startMatch(self):

        while True:

            # TODO handle case when no one wins
            # check if the game has been won
            if self.getWinner():
                print("Congratulations %s, you won !" % self.currentPlayer.name)
                break

            self.currentPlayer = self.nextPlayer()
            square = self.promptPlayerMove(self.currentPlayer.name)

            try:
                self.board.markBoard(square, self.currentPlayer.letter)
                self.board.printBoard()

            except(TakenSquareException) as e:
                print(e.args[0])

    '''
        Checks the board for a winning player

        :return True if the game has been won, false otherwise
    '''

    def getWinner(self):
        squares = self.board.squares

        # TODO use threads to check columns, rows, and crosses indipendently
        if (not str.isspace(squares[0]) and squares[0] == squares[1] == squares[2]) or \
                (not str.isspace(squares[3]) and squares[3] == squares[4] == squares[5]) or \
                (not str.isspace(squares[6]) and squares[6] == squares[7] == squares[8]) or \
                (not str.isspace(squares[0]) and squares[0] == squares[3] == squares[6]) or \
                (not str.isspace(squares[1]) and squares[1] == squares[4] == squares[7]) or \
                (not str.isspace(squares[2]) and squares[2] == squares[5] == squares[8]) or \
                (not str.isspace(squares[0]) and squares[0] == squares[4] == squares[8]) or \
                (not str.isspace(squares[2]) and squares[2] == squares[4] == squares[6]):
            return True

        return False

    '''
        Purpose:
            
    '''
    def nextPlayer(self):

        if self.currentPlayer is self.players[0]:
            return self.players[1]

        return self.players[0]


    '''
        Adds a player to the game
        
        :arg player object to add to the game
    '''
    def addPlayer(self, player):
        self.players.append(player)

    '''
        Prompts the player to select a square to make a move  
    '''
    def promptPlayerMove(self, player):

        square = ' '
        while not square.isnumeric() or re.search('^[1-9]$', square) == None:
            square = input("%s, place %c on a square (1 - 9)" %(player, self.currentPlayer.letter)).strip()

        return square


class Player:

    '''
        Player has a name and an assigned piece to make moves
    '''
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter


'''
    Author:
        Isaac Buitrago
        
    Purpose:
        Responsible for maintaining the
        states of individual squares in the board
'''
class Board:

    ROW_COL_SIZE = 3

    def __init__(self):
        self.squares = [' ' for i in range(9)]

    '''
        Responsible for printing the contents of the board
    '''
    def printBoard(self):

        # index for slicing
        i = 0
        j = 3

        while j <= len(self.squares):
            row = self.squares[i:j]
            print('|%c|%c|%c|' %(row[0], row[1], row[2]))
            i = j
            j += 3

    '''
        Purpose:
            Used to mark a square with the given letter

        Parameters:
            square - square number on board
            
        Notes:
            Assume that square has been validated to be 1-9
    '''
    def markBoard(self, square, letter):

        # check for valid square index and unmarked square
        if self.squares[int(square) - 1] != ' ':
            raise TakenSquareException('Square has been marked')

        else:
            self.squares[int(square) - 1] = letter

    '''
        Purpose:
            Clears a board by setting each square to it's default value      
    '''
    def clearBoard(self):
        for i, x in enumerate(self.squares):
            if x != ' ':
                self.squares[i] = ' '



