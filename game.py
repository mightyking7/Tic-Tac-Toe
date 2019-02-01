
import re
from exceptions import InvalidSquareException

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
        self.winner = None
        self.players = []

    '''
        Starts a new match
    '''
    def startMatch(self):

        self.currentPlayer = self.players[0]
        square = self.promptPlayerMove(self.currentPlayer.name)

        try:
            self.board.markBoard(square, self.currentPlayer.letter)
            self.board.printBoard()

        except(InvalidSquareException) as e:
            print(e.args[0])



    '''
        Used to add a player to the game
        
        player - Player object to add to the game
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
            raise InvalidSquareException('Invalid square selected')

        else:
            self.squares[int(square) - 1] = letter


