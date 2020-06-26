"""
Tic Tac Toe Player
"""

import math
import copy
import random
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
    xs = 0
    os = 0
    for row in board:
        for col in row:
            if col == X:
                xs +=1
            elif col == O:
                os += 1
    if xs > os:
        return O
    else:
        return X
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    p_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                p_actions.add((i, j))
    return p_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move")
    elif terminal(board):
        raise Exception("Terminal")
    else:
        new_board = copy.deepcopy(board)
        (i, j) = action
        new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None: 
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == [[EMPTY] * 3] * 3:
        return (random.randint(0, 2), random.randint(0, 2))
    if terminal(board):
        return None
    p = player(board)
    selected_action = None
    if p == X:
        #Maximize the score
        v = float('-inf')
        for action in actions(board):
            mxv = minv(result(board, action))
            if mxv > v:
                v = mxv
                selected_action = action
        return selected_action
    if p == O:
        #Minimize the score
        v = float('inf')
        for action in actions(board):
            mnv = maxv(result(board, action))
            if mnv < v:
                v = mnv
                selected_action = action
        return selected_action

def maxv(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, minv(result(board, action)))
    return v

def minv(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, maxv(result(board, action)))
    return v