"""
Tic Tac Toe Player
"""

import math, copy, sys

X = "X"
O = "O"
EMPTY = None

possibilities = set()

sys.setrecursionlimit(26830)

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
   
    
    for row in range(3):
        # print("ROW : " + str(row))
        for column in range(3):
            # print("COLUMN : " + str(column))
            #This seems to not work very well , does add just few items, it is a set, i think it will treat 1,0 same as 0,1
            if board[row][column] is EMPTY:
                # print("ADDED : " + str(row) + ", " + str(column))
                possibilities.add((row,column))
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        new_board = copy.deepcopy(board)
        
        row, column = action
        if action in possibilities:
            new_board[row][column] = player(new_board)
            actions(new_board)
            return new_board
        else:
            return new_board
    except:
        raise TypeError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for row in board:
        if row.count("X") == 3:
            return "X"
        if row.count("O") == 3:
            return "O"
    rotated_board = list(zip(board[::-1]))
    for column in rotated_board:
        if column.count("X") == 3:
            return "X"
        if column.count("O") == 3:
            return "O"
    diagonals = [[],[]]
    for row in range(len(board)):
        for column in range(row):
            if row == column and row is not EMPTY:
                diagonals[0].append(board[row][column])
                if row == 1 and column == 1:
                    diagonals[1].append(board[row][column])
            if row + 2 == column or row == column + 2 and row is not EMPTY:
                diagonals[1].append(board[row][column])
    for diagonal in diagonals:
        if diagonal.count("X") == 3:
            
            return "X"
        if diagonal.count("O") == 3:
            
            return "O"
    if len(possibilities) == 0:
        
        return None

    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    if board.count(EMPTY) == 0:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    for possible_move in possibilities:
        final = recursive_play(board, possible_move)
        if player(board) == "X":
            if final == 1:
                print("1")
                return possible_move
        if player(board) == "O":
            if final == -1:
                print("-1")
                return possible_move
            

def recursive_play(board, action):
    while not terminal(board):
        new_board = result(board, action)
        while len(possibilities) > 0:
            print("New iteration")
            for possible_move in possibilities:
                print(possible_move)
                recursive_play(board,possible_move)
    
    return utility(board)   
