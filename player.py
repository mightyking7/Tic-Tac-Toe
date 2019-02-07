
'''
    Purpose:
        Player for a game of Tic Tac Toe

    Author:
        Isaac Buitrago
'''
class Player:

    '''
        Player has a name and an assigned piece to make moves
    '''
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
        self.moves = 0