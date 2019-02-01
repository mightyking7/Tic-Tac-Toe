import re
from game import *
'''
    Used to get the name of the user.
    Name is validated to ensure that only
    letters and spaces are accepted.
'''
def getName(message):

    name = input(message).strip()

    while not re.search(r'^([a-zA-Z\'\-]+)\s?([a-zA-Z\'\-]+)?$', name) or len(name) > 50:
        print("Name can only contain letters and spaces")

        name = input(message).strip()

    return name

'''
    Retrieves the letter a player will use in a match
'''
def getLetter():

    letter = input("Do you want to be X or O ?").strip().upper()

    # validate input
    while not (letter == 'X' or letter == 'O'):
        print("Invalid input, please try again")

        letter = input("Do you want to be X or O ?").strip().upper()

    return letter


'''
    Entry point for Tic Tac Toe game
'''
def main():

    # print welcome message and set up the project
    print("Welcome to the game of tic tac toe !")

    name1 = getName("Player 1, what is your name ?")
    letter1 = getLetter()

    name2 = getName("Player 2, what is your name ?")
    letter2 = 'O' if letter1 == 'X' else 'X'
    print("%s you are letter %c" %(name2, letter2))

    # create a new game and print the board
    game = Game()
    game.board.printBoard()
    game.addPlayer( Player(name1, letter1) )
    game.addPlayer( Player(name2, letter2) )

    # start a new match
    game.startMatch()
main()
