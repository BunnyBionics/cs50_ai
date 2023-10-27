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
    x = o = 0
    for row in board:
        for column in row:
            if column == X:
                x += 1
            if column == O:
                o += 1
    if x == o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    # maybe do row in range3: column in range3: if board[row][column] == EMPTY: etc
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                possible.add((row, column))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    # DO A DEEP COPY!  I SPENT FOUR HOURS DEBUGGING THIS!!
    copy = deepcopy(board)
    if action not in actions(board):
        raise Exception('not a valid move!')
    copy[action[0]][action[1]] = turn
    return copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3):
        for column in range(3):
            letter = board[row][column]
            if not letter:
                continue
            if row == 0:
                if letter == board[row + 1][column] == board[row + 2][column]:
                    return letter
            if column == 0:
                if board[row] == [letter, letter, letter]:
                    return letter
            if row == column == 0:
                if letter == board[1][1] == board[2][2]:
                    return letter
            if row == 0 and column == 2:
                if letter == board[1][1] == board[2][0]:
                    return letter


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    if not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    # """
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

    best = ()
    if player(board) == X:
        for move in actions(board):
            value = min_value(result(board, move))
            if not best or value > best[0]:
                best = (value, move)
        return best[1]

    if player(board) == O:
        for move in actions(board):
            value = max_value(result(board, move))
            if not best or value < best[0]:
                best = (value, move)
        return best[1]


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v
