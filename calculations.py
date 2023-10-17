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

def calculate_coordinates(x: int, y: int, width: int, height: int) -> Tuple:
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
    row = 0
    col = 0
    if x > width * 5 // 12 and x <= width * 7 // 12: col = 1
    elif x > width * 7 // 12: col = 2
    
    if y > height * 5 // 12 and y <= height * 7 // 12: row = 1
    elif y > height * 7 // 12: row = 2

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
    for row in board:
        for col in row:
            if col is None: return False

    return True

def get_x_coords(w: int, h: int) -> Dict:
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

def get_o_coords(w: int, h: int) -> Dict:
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

if __name__ == '__main__':
    assert False, '\n\nThis is a module of functions. Please import its contents into another file.\n'
