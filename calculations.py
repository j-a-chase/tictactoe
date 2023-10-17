######################################################################################################################################################
# Name: Jamaes A. Chase
# File: calculations.py
# Date: 17 October 2023
# Description:
#
# Module file holding functions that aren't members of the Engine class.
#
######################################################################################################################################################

# imports
from typing import Tuple, List, Dict
from random import choice

def calculate_coordinates(x: int, y: int, width: int, height: int) -> Tuple[int, int]:
    '''
    Calculates which grid square the drawing should be placed in depending on what the coordinates provided are.

    Parameters:
        - x: integer containing the x-value for where the mouse was clicked
        - y: integer containing the y-value for where the mouse was clicked
        - width: integer containing the width of the screen
        - height: integer containing the height of the screen

    Returns:
        - a tuple containing the corresponding indices for the board list
    '''
    # initialize row, col to (0, 0)
    row = 0
    col = 0
    
    # if click is in the second or third column, update accordingly
    if x > width * 5 // 12 and x <= width * 7 // 12: col = 1
    elif x > width * 7 // 12: col = 2
    
    # if click is in the second or third row, update accordingly
    if y > height * 5 // 12 and y <= height * 7 // 12: row = 1
    elif y > height * 7 // 12: row = 2

    # return new coordinates
    return (row, col)

def is_win(board: List[List[str]]) -> bool:
    '''
    Determines if the game has been won by either the X's or O's

    Parameters:
        - board: A 3x3 list containing values either 'X', 'O', or None

    Returns:
        - a boolean value indicating if there is a win or not
    '''
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None: return True

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None: return True

    # check both diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None: return True
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None: return True

    # no win
    return False

def is_tie(board: List[List[str]]) -> bool:
    '''
    Determines if there is a tie.

    Parameters:
        - board: A 3x3 list containing values either 'X', 'O', or None

    Returns:
        - a boolean value indicating if there is a tie or not.
    '''
    # check if a valid move still exists
    for row in board:
        for col in row:
            if col is None: return False

    # if no valid moves (we already know it's not a win if this function is being called), return True
    return True

def get_x_coords(w: int, h: int) -> Dict[str, List[Tuple[int, int]]]:
    '''
    Returns the dictionary containing values for drawing an 'X'

    Parameters:
        - w: integer containing the width of the screen
        - h: integer containing the height of the screen

    Returns:
        - a dictionary containing values for drawing an 'X'
    '''
    return {
        '(0, 0)': [(w * 7 // 24, h * 7 // 24),
                    (w * 9 // 24, h * 9 // 24),
                    (w * 9 // 24, h * 7 // 24),
                    (w * 7 // 24, h * 9 // 24)],
        '(0, 1)': [(w * 11 // 24, h * 7 // 24),
                    (w * 13 // 24, h * 9 // 24),
                    (w * 13 // 24, h * 7 // 24),
                    (w * 11 // 24, h * 9 // 24)],
        '(0, 2)': [(w * 15 // 24, h * 7 // 24),
                    (w * 17 // 24, h * 9 // 24),
                    (w * 17 // 24, h * 7 // 24),
                    (w * 15 // 24, h * 9 // 24)],
        '(1, 0)': [(w * 7 // 24, h * 11 // 24),
                    (w * 9 // 24, h * 13 // 24),
                    (w * 9 // 24, h * 11 // 24),
                    (w * 7 // 24, h * 13 // 24)],
        '(1, 1)': [(w * 11 // 24, h * 11 // 24),
                    (w * 13 // 24, h * 13 // 24),
                    (w * 13 // 24, h * 11 // 24),
                    (w * 11 // 24, h * 13 // 24)],
        '(1, 2)': [(w * 15 // 24, h * 11 // 24),
                    (w * 17 // 24, h * 13 // 24),
                    (w * 17 // 24, h * 11 // 24),
                    (w * 15 // 24, h * 13 // 24)],
        '(2, 0)': [(w * 7 // 24, h * 15 // 24),
                    (w * 9 // 24, h * 17 // 24),
                    (w * 9 // 24, h * 15 // 24),
                    (w * 7 // 24, h * 17 // 24)],
        '(2, 1)': [(w * 11 // 24, h * 15 // 24),
                    (w * 13 // 24, h * 17 // 24),
                    (w * 13 // 24, h * 15 // 24),
                    (w * 11 // 24, h * 17 // 24)],
        '(2, 2)': [(w * 15 // 24, h * 15 // 24),
                    (w * 17 // 24, h * 17 // 24),
                    (w * 17 // 24, h * 15 // 24),
                    (w * 15 // 24, h * 17 // 24)]
    }

def get_o_coords(w: int, h: int) -> Dict[str, List[Tuple[int, int]]]:
    '''
    Returns the dictionary containing values for drawing an 'O'

    Parameters:
        - w: integer containing the width of the screen
        - h: integer containing the height of the screen

    Returns:
        - a dictionary containing values for drawing an 'X'
    '''
    return {
        '(0, 0)': [w * 7 // 24, h * 7 // 24],
        '(0, 1)': [w * 11 // 24, h * 7 // 24],
        '(0, 2)': [w * 15 // 24, h * 7 // 24],
        '(1, 0)': [w * 7 // 24, h * 11 // 24],
        '(1, 1)': [w * 11 // 24, h * 11 // 24],
        '(1, 2)': [w * 15 // 24, h * 11 // 24],
        '(2, 0)': [w * 7 // 24, h * 15 // 24],
        '(2, 1)': [w * 11 // 24, h * 15 // 24],
        '(2, 2)': [w * 15 // 24, h * 15 // 24]
    }

def computer_move(board: List[List[str]]) -> Tuple[int, int]:
    '''
    This function controls the computer's moves if you desire to play with a computer opponent.

    Parameters:
        - board: a 3x3 list containing either 'X', 'O', or None
    
    Returns:
        - a tuple containing the coordinates where the CPU moved, or None if the CPU has no move available (shouldn't be possible if coded correctly).
    '''
    # grab empty squares
    empties = [(x, y) for x in range(3) for y in range(3) if board[x][y] is None]

    # if empty squares exist (might not need this check...)
    if empties:
        # pick a random square
        x, y = choice(empties)

        # update internal board
        board[x][y] = 'O' # computer will always be O's

        # return indices to update GUI
        return (x, y)
    
    # return None if no move exists (again, probably don't need this)
    return None

if __name__ == '__main__': assert False, '\n\nThis is a module of functions. Please import its contents into another file.\n'
