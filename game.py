
import re
from sys import maxsize


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
        Purpose:
            Starts a new match
            
        Notes:
            Starts an infinite loop that runs until a 
            player has won or a tie has occured
    '''
    def startMatch(self):

        while True:

            # get the next player
            self.currentPlayer = self.nextPlayer()
            currentPlayer = self.currentPlayer

            # prompt the player to make a move
            square = self.promptPlayerMove()

            # mark the square with the letter
            self.board.markBoard(square, currentPlayer.letter)
            currentPlayer.moves += 1

            self.board.printBoard()

            # check if the game has been won
            if currentPlayer.moves >= 3 and Game.isWinner(self.board, currentPlayer.letter):
                print("Congratulations %s, you won !" % currentPlayer.name)
                break

            # tie if X and O are only elements in the board
            elif currentPlayer.moves >= 3 and len(set(self.board.squares)) == 2:
                print("Tie!")
                break

    '''
        Purpose:
            Checks if board has been conquered by a player's letter
        
        Parameters:
            l -  letter to check for a winner
            
        Notes:
            Checks if any row, column, or cross on the board contain the given letter 

        Returns:
            True if a row, column, or cross contain l
            False otherwise
    '''
    @classmethod
    def isWinner(cls, board, l):

        squares = board.squares

        if squares[0] == squares[1] == squares[2]  == l or \
            squares[3] == squares[4] == squares[5] == l or \
            squares[6] == squares[7] == squares[8] == l or \
            squares[0] == squares[3] == squares[6] == l or \
            squares[1] == squares[4] == squares[7] == l or \
            squares[2] == squares[5] == squares[8] == l or \
            squares[0] == squares[4] == squares[8] == l or \
            squares[2] == squares[4] == squares[6]:
                return True

        return False

    '''
        Purpose:
            Returns the next player to make a move
    '''
    def nextPlayer(self):

        if self.currentPlayer is self.players[0]:
            return self.players[1]

        return self.players[0]


    '''
        Purpose:
            Adds a player to the game
        
        Parameters:
            player -  player to add
    '''
    def addPlayer(self, player):
        self.players.append(player)


    '''
        Purpose:
            Prompts the player to select which square to make a move on
            
        Notes:
            The player will continue to be prompted
            as long as they have provided invalid input.
            
            Valid input is a numeric value 1-9 that has
            not been occupied on the board.
            
        Parameters:
            player - prompts the player to make a move  
            
        Return: 
            Number of Square  
            
    '''
    def promptPlayerMove(self):

        square = ' '
        while not square.isnumeric() or \
              re.search('^[1-9]$', square) == None or \
              self.board.squares[int(square) - 1] != ' ':

            square = input("%s, place %c on a square (1 - 9)"\
                        %(self.currentPlayer.name, self.currentPlayer.letter)).strip()

        return int(square)


class Player:

    '''
        Player has a name and an assigned piece to make moves
    '''
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
        self.moves = 0


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
        self.squares = [' '] * 9

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
            Assume that square is a number 1-9
    '''
    def markBoard(self, square, letter):
            self.squares[square - 1] = letter

    '''
        Purpose:
            Clears a board by setting each square to it's default value      
    '''
    def clearBoard(self):
        for i, x in enumerate(self.squares):
            if x != ' ':
                self.squares[i] = ' '












