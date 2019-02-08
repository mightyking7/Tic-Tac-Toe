
import re
from agent import Agent
from board import Board

'''
    Author: 
        Isaac Buitrago 

    Purpose:   
        Responsible for controlling state of game
        and determining the winner of a match
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
            player has won or a tie has occurred
    '''
    def startMatch(self):

        while True:

            # get the next player
            self.currentPlayer = self.nextPlayer()
            currentPlayer = self.currentPlayer

            # prompt the player for their letter
            square = self.promptPlayerMove()

            # mark the square and increment the number of moves for the player
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
            squares[2] == squares[4] == squares[6] == l:
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

        squares = self.board.squares
        square = ' '

        message = f"{self.currentPlayer.name}, place {self.currentPlayer.letter} on a square (1 - 9) that is not occupied: "

        # while input is not valid
        while not square.isnumeric() or re.search('^[1-9]$', square) == None or squares[int(square) - 1] != ' ':
            square = input(message).strip()

        return int(square)

















