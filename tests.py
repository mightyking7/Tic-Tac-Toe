import unittest
from game import *
from player import *


'''
    Author:
        Isaac Buitrago
        
    Purpose:
        Tests for validating if the Tic Tac Toe game works
'''
class TestGame(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.rows = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        cls.cols = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        cls.crosses = [(1, 5, 9), (3, 5, 7)]

    '''
        Purpose:
            Used to validate if a player can mark a square with their letter
    '''
    def test_markBoard(self):

        player1 = Player('X', 'X')

        self.game.addPlayer(player1)

        board = self.game.getBoard()

        board.markBoard(1, player1)

        squareMark = board.getSquare(1)

        playerLetter = player1.getLetter()

        self.assertEqual(squareMark.name, playerLetter)

        board.clearBoard()

    '''
        Purpose:
            Used to validate if a player can dominate three adjacent cells
    '''
    def test_GameWon(self):

        player1 = Player('X', 'X')
        player2 = Player('O', 'O')

        self.game.addPlayer(player1)
        self.game.addPlayer(player2)

        # test if player1 can win the game
        self.canConquerRow(player1)
        self.canConquerColumn(player1)
        self.canConquerCross(player1)

        # test if player2 can win the game
        self.canConquerRow(player2)
        self.canConquerColumn(player2)
        self.canConquerCross(player2)


    '''
        Purpose:
            Used to test if a game can result in a draw
            such that player1 and player2 block each other
    '''
    def test_GameTie(self):

        board = self.game.getBoard()

        player1 = Player('X', 'X')
        player2 = Player('O', 'O')

        self.game.addPlayer(player1)
        self.game.addPlayer(player2)

        player1 = self.game.players[0] # x
        player2 = self.game.players[1] # o


        '''
            State of board when a draw occurs
        
            |x|x|o|
            |o|o|x|
            |x|o|x|
        '''
        board.markBoard(1, player1.letter)
        board.markBoard(2, player1.letter)
        board.markBoard(3, player2.letter)
        board.markBoard(4, player2.letter)
        board.markBoard(5, player2.letter)
        board.markBoard(6, player1.letter)
        board.markBoard(7, player1.letter)
        board.markBoard(8, player2.letter)
        board.markBoard(9, player1.letter)

        # neither player1 or player2 won, draw
        p1Won = Game.isWinner(board, player1.letter)
        p2Won = Game.isWinner(board, player1.letter)

        self.assertFalse(p1Won)
        self.assertFalse(p2Won)

        board.clearBoard()

    '''
        Purpose:
            Used to validate if the board allows 
            a player to overwrite an opponents square.
    '''
    def test_MakeLegalMoves(self):

        board = self.game.getBoard()

        player1 = Player('X', 'X')
        player2 = Player('O', 'O')

        self.game.addPlayer(player1)
        self.game.addPlayer(player2)

        validMove   = board.markBoard(1, player1.letter)
        invalidMove = board.markBoard(1, player2.letter)

        self.assertTrue(validMove)
        self.assertFalse(invalidMove)

        board.clearBoard()



    '''
        Purpose:
            Asserts that the player can mark any row with their letter
        
        Notes:
            Clears the board at the end of each iteration
            
        Parameters:
            player - player to test 
    '''
    def canConquerRow(self, player):

        board = self.game.getBoard()

        for row in self.rows:
            board.markBoard(row[0], player.letter)
            board.markBoard(row[1], player.letter)
            board.markBoard(row[2], player.letter)
            win = Game.isWinner(self.game.board, player.letter)

            self.assertTrue(win)
            board.clearBoard()

    '''
        Purpose:
            Asserts that the player can mark any column with their letter
            
        Notes:
            Clears the board at the end of each iteration
            
        Parameters:
            player - player to test
    '''
    def canConquerColumn(self, player):

        board = self.game.getBoard()

        for col in self.cols:
            board.markBoard(col[0], player.letter)
            board.markBoard(col[1], player.letter)
            board.markBoard(col[2], player.letter)
            win = Game.isWinner(self.game.board, player.letter)

            self.assertTrue(win)
            board.clearBoard()

    '''
        Purpose:
            Asserts that the player can mark any cross with their letter
        
        Notes:
            Clears the board at the end of each iteration
            
        Parameters:
            player - player to test
    '''
    def canConquerCross(self, player):

        board = self.game.getBoard()

        for cross in self.crosses:
            board.markBoard(cross[0], player.letter)
            board.markBoard(cross[1], player.letter)
            board.markBoard(cross[2], player.letter)
            win = Game.isWinner(self.game.board, player.letter)

            self.assertTrue(win)
            board.clearBoard()

    if __name__ == '__main__':
        unittest.main()

