import unittest
from game import *
from player import *


'''
    Purpose:
        Tests for verifying that the game of Tic Tac Toe works
'''
class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.rows = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        cls.cols = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        cls.crosses = [(1, 5, 9), (3, 5, 7)]

    '''
        Tests if marking any three squares with the same letter results in a winner
    '''
    def test_GameWon(self):

        player1 = Player('X', 'X')
        player2 = Player('O', 'O')

        self.game.addPlayer(player1)
        self.game.addPlayer(player2)

        self.canConquerRow(player1)
        self.canConquerColumn(player1)
        self.canConquerCross(player1)

        self.canConquerRow(player2)
        self.canConquerColumn(player2)
        self.canConquerCross(player2)

    '''
        Purpose:
            Asserts that the player can mark any row with their letter
            
        Parameters:
            player - player to test 
    '''
    def canConquerRow(self, player):

        board = self.game.board

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
            
        Parameters:
            player - player to test
    '''
    def canConquerColumn(self, player):

        board = self.game.board

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
            
        Parameters:
            player - player to test
    '''
    def canConquerCross(self, player):

        board = self.game.board

        for cross in self.crosses:
            board.markBoard(cross[0], player.letter)
            board.markBoard(cross[1], player.letter)
            board.markBoard(cross[2], player.letter)
            win = Game.isWinner(self.game.board, player.letter)

            self.assertTrue(win)
            board.clearBoard()

    if __name__ == '__main__':
        unittest.main()
