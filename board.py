
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
        Purpose:
            Gets the squares for the board
    '''
    def getSquares(self):
        return self.squares

    '''
        Purpose:
            Returns the letter at the given index
        
        Parameters:
            index - index into squares that is not zero off-setted
    '''
    def getSquare(self, index):

        if index in range(len(self.squares)):
            return self.squares[index - 1]

        return None

    '''
        Purpose:
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