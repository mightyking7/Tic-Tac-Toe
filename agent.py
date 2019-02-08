from player import Player
from sys import maxsize
import game as g

'''
    Author:
        Isaac Buitrago
        
    Purpose:
        Autonomous agent that plays against a human player.

    Notes:
        Utilizes the minimax search algorithm 
        to find a move that minimizes the 
        maximum possible loss in a game tree.
'''
class Agent(Player):

    '''
        Purpose:
            Constructor

        Parameters:
            board - board to make a move on
            opponent - player to minimize performance
    '''
    def __init__(self, name, letter, board, opponent):

        super().__init__(name, letter)

        self.board = board        # board to analyze

        self.opponent = opponent  # opponent in game

    '''
        Purpose:
            Gets the best board index for the agent to select.

        Returns:
            Optimal index on the board
    '''
    def getNextMove(self):

        # get index with max score
        score = self.minimax(2, self)

        return score[0]


    '''
        Purpose:
            Calculates the optimal index the agent should select
            
        Returns:
            Optimal index on the board
    '''
    def minimax(self, depth, player):

        # default move for player
        move = -1

        if type(player) is Agent:
            best = [move, -maxsize]

        else:
            best = [move, maxsize]

        # get legal moves for player
        moves = self.getMoves(self.board)

        # base case
        # depth reached or game is over, evaluate score
        if depth == 0 or len(moves) == 0:
            score = self.evaluate()
            return [move, score]

        else:

            for move in moves:

                # try move for player
                self.board.getSquares()[move] = player.letter

                # computer is maximizing player
                if type(player) is Agent:

                    score = self.minimax(depth - 1, self.opponent)

                    if score[1] > best[1]:
                        best = score
                        best[0] = move

                # opponent is minimizing player
                else:
                    score = self.minimax(depth - 1, self)

                    if score[1] < best[1]:
                        best = score
                        best[0] = move

                # undo move
                self.board.getSquares()[move] = ' '

        return best


    '''
        Purpose:
            Returns all valid moves the agent can select
            or an empty list if no legal moves are possible
        
        Returns:
            List of legal indices that the agent 
            can move into given the current state of the board.
    '''

    def getMoves(self, board):

        moves = []

        # game over, no next move
        if g.Game.isWinner(board, 'X') or g.Game.isWinner(board, 'O'):
            return moves

        # get index of available squares
        for i, val in enumerate(board.getSquares()):
            if val == ' ':
                moves.append(i)

        return moves

    '''
        Purpose:
            Heuristic evaluation function for the board

        Returns:
            100, 10, 1 for each 3 - 2 - 1 in a line for computer
            -100, -10, -1 for each 3 - 2 - 1 in a line for opponent
             0 otherwise
    '''

    def evaluate(self):

        score = 0

        # get score for rows  1-3
        score += self.evaluateLine(0, 1, 2)
        score += self.evaluateLine(3, 4, 5)
        score += self.evaluateLine(6, 7, 8)

        # get score for columns 1-3
        score += self.evaluateLine(0, 3, 6)
        score += self.evaluateLine(1, 4, 7)
        score += self.evaluateLine(2, 5, 8)

        # get score for diagonals
        score += self.evaluateLine(0, 4, 8)
        score += self.evaluateLine(2, 4, 6)

        return score

    '''
        Purpose:
            Heuristic evaluation function for the line on a board

        Parameters:
            cell1 - index of square on the board
            cell2 - index of square on the board
            cell3 - index of square on the board

        Returns:
            100, 10, 1 for each 3 - 2 - 1 in a line for computer
            -100, -10, -1 for each 3 - 2 - 1 in a line for opponent
             0 otherwise
    '''

    def evaluateLine(self, cell1, cell2, cell3):

        squares = self.board.getSquares()

        opLetter = self.opponent.getLetter()

        score = 0

        # first cell
        if squares[cell1] == self.letter:
            score = 1

        elif squares[cell1] == opLetter:
            score = -1

        # second cell
        if squares[cell2] == self.letter:

            # cell1 has letter of agent
            if score == 1:
                score = 10

            # cell1 has letter of opponent
            elif score == -1:
                return 0

            # cell1 is empty
            else:
                score = 1

        elif squares[cell2] == opLetter:
            # cell1 has letter of opponent
            if score == -1:
                score = -10

            # cell1 has letter of agent
            elif score == 1:
                return 0

            # cell1 is empty
            else:
                score = -1

        # third cell
        if squares[cell3] == self.letter:

            # cell has letter of agent
            if score > 0:
                score *= 10

            # cell1 and or cell2 has letter of opponent
            elif score < 0:
                return 0

            # cell1 and cell2 are empty
            else:
                score = 1

        elif squares[cell3] == opLetter:

            # cell1 and or cell2 has letter of opponent
            if score < 0:
                score *= 10

            # cell1 and or cell2 has letter of agent
            elif score > 0:
                return 0
            # cell1 and or cell2 are empty
            else:
                score = -1

        return score


