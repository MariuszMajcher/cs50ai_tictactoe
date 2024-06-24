"""
Tic Tac Toe Player
"""

import math, copy, sys

X = "X"
O = "O"
EMPTY = None


sys.setrecursionlimit(26830)

# I guess it does not pass in the cs50 as it uses its own runner.py file, need to 
# make all the functionality inside this file

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
    empty = 0
    
    for row in board:
        empty += row.count(EMPTY)
    if empty % 2 == 1:
        return "X"
    else:
        return "O"
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibible_moves = set()
    
    for row in range(3):
        for column in range(3):
            if board[row][column] is EMPTY:
                possibible_moves.add((row,column))
    return possibible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
 
        row, column = action
        if action in actions(board):
            new_board = copy.deepcopy(board)
            new_board[row][column] = player(new_board)
           
            return new_board
        
    except:
        raise ValueError("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for row in board:
        if row.count("X") == 3:
            return "X"
        if row.count("O") == 3:
            return "O"
    rotated_board = list(zip(*board[::-1]))
   
    for column in rotated_board:

        if column.count("X") == 3:
            return "X"
        if column.count("O") == 3:
            return "O"
    diagonal_left = []
    diagonal_right = []
    for row in range(3):
        for column in range(3):
            if  row == 0 and column == 0:
                diagonal_left.append(board[row][column])
            if  row == 1 and column == 1:
                diagonal_left.append(board[row][column])
                diagonal_right.append(board[row][column])
            if  row == 2 and column == 2:
                diagonal_left.append(board[row][column])
            if  row == 0 and column == 2:
                diagonal_right.append(board[row][column])
            if row == 2 and column == 0:
                diagonal_right.append(board[row][column])
    if diagonal_left.count("X") ==3:
        return "X"
    if diagonal_left.count("O") == 3:
        return "O"
    if diagonal_right.count("X") == 3:
        return "X"
    if diagonal_right.count("O") == 3:
        return "O"
    else:
        return None

    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == "X" or winner(board) == "O" or sum([row.count(EMPTY) for row in board]) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X":
            return 1
        if winner(board) == "O":
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    

    current_player = player(board) 
    
    if current_player == "O":
        array_of_moves = []
        
        for action in actions(board):
            array_of_moves.append([action, max_value(result(board, action))])
        initial_value = math.inf
        for action, value in array_of_moves:
            if value < initial_value:
                initial_value = value
                move = action
        return move
    
    if current_player == "X":
        array_of_moves = []
        
        for action in actions(board):
            array_of_moves.append([action, min_value(result(board, action))])
        initial_value = -math.inf
        for action, value in array_of_moves:
            if value > initial_value:
                
                initial_value = value
                move = action
        return move

def min_value(board):
    """
    Will want to choose the move that leads to minimum value
    """
    if terminal(board):
       return utility(board)
    v = math.inf
    for action in actions(board):

        v = min(v, max_value(result(board, action)))
    return v
    
def max_value(board):
    """
    Will want to choose the move that leads to maximum value
    """
    
    if terminal(board):
       return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v