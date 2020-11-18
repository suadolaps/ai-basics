"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = no_of_moves_made(board)

    if count % 2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    player_turn = player(board)


    if new_board[action[0]][action[1]] != EMPTY:
        print("Choose another action, space occupied")
    else:
        new_board[action[0]][action[1]] = player_turn
        
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_positions = [
        ((0, 0), (0, 1), (0,2)), 
        ((1, 0), (1, 1), (1,2)), 
        ((2, 0), (2, 1), (2,2)), 
        ((0, 0), (1, 0), (2,0)), 
        ((0, 1), (1, 1), (2,1)), 
        ((0, 2), (1, 2), (2,2)), 
        ((0, 0), (1, 1), (2,2)), 
        ((2, 0), (1, 1), (0,2)), 
    ]

    for (a, b), (c, d), (e, f) in winning_positions:
        if board[a][b] != EMPTY or board[c][d] != EMPTY or board[e][f] != EMPTY:
            if board[a][b] == board[c][d] == board[e][f]:
                return board[a][b]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = no_of_moves_made(board)

    if winner(board) or count == 9:
        return True
    else: 
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: 
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal_action = None

    if player(board) == X:
        optimal_util = float('-inf')
    else:
        optimal_util = float('inf')

    for action in actions(board):
        new_board = result(board, action)

        if terminal(new_board):
            util = utility(new_board)
        else:
            util = minimax(new_board)[1]
        
        if player(board) == X:
            if util > optimal_util:
                optimal_util = util
                optimal_action = action
        else:
            if util < optimal_util:
                optimal_util = util
                optimal_action = action

    return optimal_action, optimal_util 


def no_of_moves_made(board):

    count = 0

    for row in board:
        for field in row:
          if field != EMPTY:
              count += 1
    return count  