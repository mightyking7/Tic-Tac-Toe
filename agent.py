from game import Player

'''
    Purpose:
        Agent that plays against the user.

    Notes:
        Utilizes the minimax search algorithm with 
        an alpha-beta pruning tree to find the optimal move on the board.
'''


class Agent(Player):
    '''
        Purpose: Constructor

        Parameters:
            board - board to make a move on
            opponent -  player to minimize performance
    '''

    def __init__(self, board, opponent):
        super().__init__()
        self.board = board
        self.opponent = opponent

    '''
        Purpose:
            Calculates the optimal index that the agent should select
    '''

    def minimax(self, depth, player, alpha, beta):

        moves = self.getMoves(self.board)

        # agent letter is maximizing, player's letter is minimizing
        move = -1

        # game over or depth reached, evaluate score
        if len(moves) == 0 or depth == 0:
            score = self.evaluate()

            return [score, move]

        else:

            for move in moves:

                # try move for agent
                self.board.squares[move] = self.letter

                # computer is maximizing player
                if player is Agent:
                    score = self.minimax(depth - 1, self.opponent, alpha, beta)[0]

                    if score > alpha:
                        alpha = score


                # opponent is minimizing player
                else:
                    score = self.minimax(depth - 1, self, alpha, beta)[0]

                    if score < beta:
                        beta = score

                # undo move
                self.board.squares[move] = ' '

                if alpha >= beta:
                    break

        return [alpha if player is Agent else beta, move]

    '''
     Purpose:
        Returns all valid moves the agent can select
        or an empty list if no legal moves are possible
    '''

    def getMoves(self, board):

        moves = []

        # game over, no next move
        if Game.isWinner(board, 'X') or Game.isWinner(board, 'O'):
            return moves

        # get index of available squares
        for i, val in enumerate(board.squares):
            if val == ' ':
                moves.append(i)

        return moves

    '''
        Purpose:
            Heuristic evaluation function for the board

        Return:
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

        Return:
            100, 10, 1 for each 3 - 2 - 1 in a line for computer
            -100, -10, -1 for each 3 - 2 - 1 in a line for opponent
             0 otherwise
    '''

    def evaluateLine(self, cell1, cell2, cell3):
        pass
