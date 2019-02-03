import unittest
from game import *

class TestGame(unittest.TestCase):


    '''
        Tests if marking any three squares with the same piece calculates a winner
    '''
    def test_GameWon(self):

        letter = 'X'

        game = Game()

        player1 = Player('X', 'X')
        player2 = Player('O', 'O')

        game.addPlayer(player1, player2)




    if __name__ == '__main__':
        unittest.main()
