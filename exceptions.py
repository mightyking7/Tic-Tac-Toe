'''
    Author: Isaac Buitrago

    Purpose:
        Raised if user selects invalid square
'''
class InvalidSquareException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)