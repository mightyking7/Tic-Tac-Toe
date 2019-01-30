import re
from Game import *

'''
    Entry point for Tic Tac Toe game
    
    Isaac Buitrago
'''

def getName(message):

    name = input(message).strip()

    while not re.search(r'^([a-zA-Z\'\-]+|\s{1})$', name) or len(name) > 50:
        print("Invalid input, please try again")

        name = input(message).strip()

def main():

    print("Greetings, Welcome to the game of tic tac toe !")

    name1 = getName("Player 1, what is your name ?")

    name2 = getName("Player 2, what is your name ?")

    letter = input("Do you want to be X or O ?").strip().upper()

    # validate input
    while not re.match('^[OX]$', letter) or len(letter) > 1:

        print("Invalid input, please try again")

        letter = input("Do you want to be X or O ?").strip().upper()

    game = Game()

    # print board
    game.printBoard()

    # get name of players

main()
