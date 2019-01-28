import re
import Game

def main():

    print("Greetings, Welcome to the game of tic tac toe !")

    letter = input("Do you want to be X or O ?").strip().upper()

    # validate input
    while re.match('^[OX]$', letter) == None:

        print('Sorry that was not a valid letter.')

        letter = input("Do you want to be X or O ?").strip().upper()

    game = Game()

    # print board
    game.printBoard()





main()