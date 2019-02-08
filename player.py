
'''

  Author:
        Isaac Buitrago

    Purpose:
        Player for a game of Tic Tac Toe

'''
class Player:

    '''
        Player has a name and an assigned piece to make moves
    '''
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
        self.moves = 0

    '''
        Getters and Setters for Player attributes
    '''
    def getLetter(self):

        return self.letter

    def getName(self):

        return self.name

    def getMoves(self):

        return self.moves

    def setMoves(self, num):

        self.moves = num