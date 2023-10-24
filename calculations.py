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

def is_win(board: List[List[str]]) -> Tuple[bool, List[Tuple[int, int]]]:
    '''
    Determines if the game has been won by either the X's or O's

    Parameters:
        - board: A 3x3 list containing values either 'X', 'O', or None

    Returns:
        - a boolean value indicating if there is a win or not
    '''
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None: return True, [(row, 0), (row, 1), (row, 2)]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None: return True, [(0, col), (1, col), (2, col)]

    # check both diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None: return True, [(0, 0), (1, 1), (2, 2)]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None: return True, [(2, 0), (1, 1), (0, 2)]

    # no win
    return False, None

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
        - a dictionary containing values for drawing an 'O'
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

def ai_computer_move(board: List[List[str]], dif: int) -> Tuple[int, int]:
    '''
    Controls the computer's moves using a simple minimax algorithm.

    Parameters:
        - board: a 3x3 list containing either 'X', 'O', or None
        - dif: an integer indicating the strength of the heuristic function (1: normal, >=2: impossible)

    Returns:
        - a tuple containing the coordinates where the CPU moved
    '''
    def heuristic_eval(board: List[List[str]]) -> int:
        '''
        A heuristic function to weight the moves of the computer AI.

        Parameters:
            - board: a 3x3 list indicating the current board state given the computer's move to a particular square.

        Returns:
            - an integer indicating the heuristic score for the computer if it would make a particular move.
        '''
        # initial score of zero
        score = 0

        # array of valid wins
        valid_wins = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        # for each win case, weight scores accordingly
        for win in valid_wins:

            # grabs 'current' board state for each win state ('current' is technically the case of if the bot has moved, but it hasn't yet)
            line = [board[row][col] for row, col in win]

            # if win, weight score heavily
            if line.count('O') == 3: score += 50
            # if blocking opponent win, weight heavily
            elif line.count('X') == 2 and line.count('O') == 1: score += 15
            # if play is made in the lane of opponent, increase score (blocks them from winning that lane)
            elif line.count('X') == 1 and line.count('O') == 1: score += 7
            # if play is in an empty lane, increase score slightly
            elif line.count('O') == 1 and line.count(None) == 2: score += 4
            # if opponent has dominance of a lane, increase score more slightly
            elif line.count('X') == 1 and line.count(None) == 2: score += 3

        # increase score of middle if available
        if board[1][1] == 'O': score += 6

        # store boolean values for if the opposing corner is open
        opp_corners = [
            board[0][0] == 'O' and board[2][2] is None,
            board[0][2] == 'O' and board[2][0] is None,
            board[2][0] == 'O' and board[0][2] is None,
            board[2][2] == 'O' and board[0][0] is None
        ]
        human_corners = [
            board[0][0] == 'X' and board[2][2] is None,
            board[0][2] == 'X' and board[2][0] is None,
            board[2][0] == 'X' and board[0][2] is None,
            board[2][2] == 'X' and board[0][0] is None
        ]

        # adjust score for opposing corners
        for o in opp_corners:
            if o: score += 5
        for x in human_corners:
            if x: score -= 5

        # if a corner is controlled, adjust score
        for row, col in [(0,0), (0, 2), (2, 0), (2, 2)]:
            if board[row][col] == 'O': score += 4
            elif board[row][col] == 'X': score -= 4
        
        # if an edge is controlled, adjust score
        for row, col in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if board[row][col] == 'O': score += 3
            elif board[row][col] == 'X': score -= 3

        # return score
        return score
    
    # initialize move and score to dummy values
    move = None
    score = -1
    
    # for each square
    for row in range(3):
        for col in range(3):
            # if it's empty
            if board[row][col] is None:
                # temporarily fill as if CPU would move there
                board[row][col] = 'O'
                
                # evaluate the score of moving to that position
                evaluation = heuristic_eval(board)

                # if impossible difficulty selected, weight blocking an opposite corner fork more, making the bot unbeatable.
                if dif > 1 and board[0][0] == board[2][2] == 'X' or board[2][0] == board[0][2] == 'X':
                    if (row, col) in [(0, 1), (1, 0), (1, 2), (2, 1)]: evaluation += 11
                
                # backtrack move
                board[row][col] = None

                # if current square's heuristic is higher, update accordingly
                if evaluation > score:
                    score = evaluation
                    move = (row, col)

    # return CPU's move
    return move

def calculate_victory_line(win_list: List[Tuple[int, int]], w: int, h: int) -> Tuple[List[int], List[int]]:
    '''
    This function calculates the needed coordinates to draw a line on the victory path on the grid.

    Parameters:
        - win_list: a list containing the grid positions of a valid win.
        - w: an integer containing the display width
        - h: an integer containing the display height

    Returns:
        - a tuple of coordinates for the victory line to be drawn at.
    '''
    # convert starting and ending tuples to strings
    start, end = str(win_list[0]), str(win_list[2])

    # if row win
    if win_list[0][0] == win_list[2][0]:
        pos = {
            '(0, 0)': [w * 7 // 24, h // 3],
            '(0, 2)': [w * 17 // 24, h // 3],
            '(1, 0)': [w * 7 // 24, h // 2],
            '(1, 2)': [w * 17 // 24, h // 2],
            '(2, 0)': [w * 7 // 24, h * 2 // 3],
            '(2, 2)': [w * 17 // 24, h * 2 // 3]
        }
    # if col win
    elif win_list[0][1] == win_list[2][1]:
        pos = {
            '(0, 0)': [w // 3, h * 7 // 24],
            '(2, 0)': [w // 3, h * 17 // 24],
            '(0, 1)': [w // 2, h * 7 // 24],
            '(2, 1)': [w // 2, h * 17 // 24],
            '(0, 2)': [w * 2 // 3, h * 7 // 24],
            '(2, 2)': [w * 2 // 3, h * 17 // 24]
        }
    # else diagonal win
    else:
        pos = {
            '(0, 0)': [w * 7 // 24, h * 7 // 24],
            '(2, 2)': [w * 17 // 24, h * 17 // 24],
            '(2, 0)': [w * 7 // 24, h * 17 // 24],
            '(0, 2)': [w * 17 // 24, h * 7 // 24]
        }

    # return drawing coordinates
    return pos[start], pos[end]

if __name__ == '__main__': assert False, '\n\nThis is a module of functions. Please import its contents into another file.\n'
