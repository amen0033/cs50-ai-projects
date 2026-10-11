"""
Tic Tac Toe Player
"""

import math

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count == o_count else O

def actions(board):
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions

def result(board, action):
    if action not in actions(board):
        raise ValueError("Invalid action")

    new_board = [row[:] for row in board]
    i, j = action
    new_board[i][j] = player(board)

    return new_board

def winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] \
                and board[0][j] != EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] \
            and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] \
            and board[0][2] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    if winner(board) is not None:
        return True

    return all(
        board[i][j] != EMPTY
        for i in range(3)
        for j in range(3)
    )

def utility(board):
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1

    return 0

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = float("-inf")
        best_action = None

        for action in actions(board):
            value = min_value(result(board, action))

            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    else:
        best_value = float("inf")
        best_action = None

        for action in actions(board):
            value = max_value(result(board, action))

            if value < best_value:
                best_value = value
                best_action = action

        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)

    value = float("-inf")

    for action in actions(board):
        value = max(value, min_value(result(board, action)))

    return value


def min_value(board):
    if terminal(board):
        return utility(board)

    value = float("inf")

    for action in actions(board):
        value = min(value, max_value(result(board, action)))

    return value
