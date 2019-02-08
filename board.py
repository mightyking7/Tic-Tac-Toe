
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
            Assume that square is a number 1-9.
            Validation is done to assure that the
            square is not populated with a letter.
            
        Returns:
            True if the board was successfully marked
            False otherwise
    '''

    def markBoard(self, square, letter):

        if self.squares[square - 1].isspace():
            self.squares[square - 1] = letter

            return True

        return False


    '''
        Purpose:
            Clears a board by setting each square to it's default value      
    '''

    def clearBoard(self):
        for i, x in enumerate(self.squares):
            if x != ' ':
                self.squares[i] = ' '