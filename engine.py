######################################################################################################################################################
# Name: James A. Chase
# File: engine.py
# Date: 16 October 2023
# Description:
#
# File containing the Engine class for running tic-tac-toe.
#
######################################################################################################################################################

# imports
import pygame
from pygame import display
from typing import Tuple, List

class Engine:
    def __init__(self, width: int = 600, height: int = 600) -> None:
        '''
        Initializes class variables for the game Engine.

        Parameters:
            - width: int with default value 600. Represents display width
            - height: int with default value 600. Represents display height

        Returns: None
        '''
        # initialize pygame assets
        pygame.init()

        # set game colors
        self.BG_COLOR = (255, 255, 255)
        self.BOARD_COLOR = (0, 0, 0)
        self.X_COLOR = (255, 0, 0)
        self.O_COLOR = (255, 165, 0)
        self.TEXT_COLOR = (50, 50, 50)

        # display dimensions
        self.w = width
        self.h = height
        
        # internal representation of game board
        self.board = [[None for x in range(3)] for y in range(3)]

        # initialize display assets
        self.window = display.set_mode((width, height))
        display.set_caption('Tic-Tac-Toe')

        # initialize fonts
        self.text_font = pygame.font.SysFont('timesnewroman', 15)
        self.turn_font = pygame.font.SysFont('timesnewroman', 25)
        self.victory_font = pygame.font.SysFont('timesnewroman', 40)

        # initialize gameplay variables
        self.turn = True

        # start game
        self.run_game()
    
    def __str__(self) -> str:
        '''
        Controls how it is handled when object is converted into a string

        Parameters: None

        Returns:
            - A string representing the tic-tac-toe grid
        '''
        s = ''
        for row in self.board:
            s += str(row) + '\n'
        return s
    
    def __repr__(self) -> str:
        '''
        Controls how Engine is represented in a more information-rich format

        Parameters: None

        Returns:
            - A string explaining the Engine class object
        '''
        return f'{__class__}\n{self.__str__()}'
    
    def clear_screen(self) -> None:
        '''
        Paints the screen the color of the background.

        Parameters: None

        Returns: None
        '''
        self.window.fill(self.BG_COLOR)
        display.update()

    def draw_grid(self) -> None:
        '''
        Draws the tic-tac-toe grid on screen

        Parameters: None

        Returns: None
        '''
        self.clear_screen()
        pygame.draw.line(self.window, self.BOARD_COLOR,
                            (self.w * 3 // 12, self.h * 5 // 12),
                            (self.w * 9 // 12, self.h * 5 // 12), 7)
        pygame.draw.line(self.window, self.BOARD_COLOR,
                            (self.w * 3 // 12, self.h * 7 // 12),
                            (self.w * 9 // 12, self.h * 7 // 12), 7)
        pygame.draw.line(self.window, self.BOARD_COLOR,
                            (self.w * 5 // 12, self.h * 3 // 12),
                            (self.w * 5 // 12, self.h * 9 // 12), 7)
        pygame.draw.line(self.window, self.BOARD_COLOR,
                            (self.w * 7 // 12, self.h * 3 // 12),
                            (self.w * 7 // 12, self.h * 9 // 12), 7)
        
        instruction_text = self.text_font.render('Click to place X or O - Q to quit', 1, self.TEXT_COLOR)
        self.window.blit(instruction_text, (self.w // 3, self.h * 5 // 6))

        turn_text = self.turn_font.render('X\'s turn.', 1, self.TEXT_COLOR)
        self.window.blit(turn_text, (self.w * 5 // 12 + (self.w // 60), self.h // 6))
        
        display.update()

    def calculate_coordinates(self, x: int, y: int, width: int, height: int) -> Tuple:
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

    def draw_xo(self, coord: Tuple[int]) -> None:
        '''
        Draws an X or O depending on whose turn it is given the coordinates of the click.

        Parameters:
            - coord: Tuple indicating which row and column were clicked

        Returns: None
        '''
        # dictionary holding the necessary coordinate values for drawing an 'X'
        x_coords = {
            '(0, 0)': [(self.w * 7 // 24, self.h * 7 // 24),
                       (self.w * 9 // 24, self.h * 9 // 24),
                       (self.w * 9 // 24, self.h * 7 // 24),
                       (self.w * 7 // 24, self.h * 9 // 24)],
            '(0, 1)': [(self.w * 11 // 24, self.h * 7 // 24),
                       (self.w * 13 // 24, self.h * 9 // 24),
                       (self.w * 13 // 24, self.h * 7 // 24),
                       (self.w * 11 // 24, self.h * 9 // 24)],
            '(0, 2)': [(self.w * 15 // 24, self.h * 7 // 24),
                       (self.w * 17 // 24, self.h * 9 // 24),
                       (self.w * 17 // 24, self.h * 7 // 24),
                       (self.w * 15 // 24, self.h * 9 // 24)],
            '(1, 0)': [(self.w * 7 // 24, self.h * 11 // 24),
                       (self.w * 9 // 24, self.h * 13 // 24),
                       (self.w * 9 // 24, self.h * 11 // 24),
                       (self.w * 7 // 24, self.h * 13 // 24)],
            '(1, 1)': [(self.w * 11 // 24, self.h * 11 // 24),
                       (self.w * 13 // 24, self.h * 13 // 24),
                       (self.w * 13 // 24, self.h * 11 // 24),
                       (self.w * 11 // 24, self.h * 13 // 24)],
            '(1, 2)': [(self.w * 15 // 24, self.h * 11 // 24),
                       (self.w * 17 // 24, self.h * 13 // 24),
                       (self.w * 17 // 24, self.h * 11 // 24),
                       (self.w * 15 // 24, self.h * 13 // 24)],
            '(2, 0)': [(self.w * 7 // 24, self.h * 15 // 24),
                       (self.w * 9 // 24, self.h * 17 // 24),
                       (self.w * 9 // 24, self.h * 15 // 24),
                       (self.w * 7 // 24, self.h * 17 // 24)],
            '(2, 1)': [(self.w * 11 // 24, self.h * 15 // 24),
                       (self.w * 13 // 24, self.h * 17 // 24),
                       (self.w * 13 // 24, self.h * 15 // 24),
                       (self.w * 11 // 24, self.h * 17 // 24)],
            '(2, 2)': [(self.w * 15 // 24, self.h * 15 // 24),
                       (self.w * 17 // 24, self.h * 17 // 24),
                       (self.w * 17 // 24, self.h * 15 // 24),
                       (self.w * 15 // 24, self.h * 17 // 24)]
        }

        # dictionary holding the necessary coordinate values for drawing an 'O'
        o_coords = {
            '(0, 0)': [self.w * 7 // 24, self.h * 7 // 24],
            '(0, 1)': [self.w * 11 // 24, self.h * 7 // 24],
            '(0, 2)': [self.w * 15 // 24, self.h * 7 // 24],
            '(1, 0)': [self.w * 7 // 24, self.h * 11 // 24],
            '(1, 1)': [self.w * 11 // 24, self.h * 11 // 24],
            '(1, 2)': [self.w * 15 // 24, self.h * 11 // 24],
            '(2, 0)': [self.w * 7 // 24, self.h * 15 // 24],
            '(2, 1)': [self.w * 11 // 24, self.h * 15 // 24],
            '(2, 2)': [self.w * 15 // 24, self.h * 15 // 24]
        }

        if self.turn: # 'X'
            shape = x_coords[str(coord)]
            pygame.draw.line(self.window, self.X_COLOR, shape[0], shape[1], 3)
            pygame.draw.line(self.window, self.X_COLOR, shape[2], shape[3], 3)

            # update internal board
            self.board[coord[0]][coord[1]] = 'X'
        else: # 'O'
            shape = o_coords[str(coord)]
            pygame.draw.ellipse(self.window, self.O_COLOR,
                                pygame.Rect(shape[0], shape[1], self.w // 12, self.h // 12), 3)
            
            # update internal board
            self.board[coord[0]][coord[1]] = 'O'
        
        # update turn text and display
        self.turn = not self.turn
        symbol = 'X' if self.turn else 'O'
        turn_text = self.turn_font.render(f'{symbol}\'s turn.', 1, self.TEXT_COLOR)
        self.window.fill(self.BG_COLOR, pygame.Rect(self.w * 5 // 12, self.h // 6, self.w // 8, self.h // 24))
        self.window.blit(turn_text, (self.w * 5 // 12 + (self.w // 60), self.h // 6))
        
        display.update()

    def is_win(self, board: List[List[str]]) -> bool:
        '''
        Determines if the game has been won by either the X's or O's

        Parameters:
            - board: a list containing strings indicating the position of the X's and O's

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
    
    def win_screen(self) -> None:
        '''
        Displays the win screen and handles events to continue or quit play.

        Parameters: None

        Returns: None
        '''
        # clear screen
        self.clear_screen()

        # grab correct symbol
        symbol = 'O' if self.turn else 'X'

        # render victory text
        victory = self.victory_font.render(f'{symbol}\'s win!', 1, self.TEXT_COLOR)
        self.window.blit(victory, (self.w * 1.25 // 3, self.h * .3))

        # render new instruction text
        instruction = self.text_font.render('Press Q to quit - Press \'Enter\' to continue playing', 1, self.TEXT_COLOR)
        self.window.blit(instruction, (self.w // 4, self.h * .4))

        # update display
        display.update()

        # handle events
        while True:
            for event in pygame.event.get():
                # quit if window closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                
                # handle keypresses
                if event.type == pygame.KEYDOWN:
                    # quit if Q is pressed
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit(0)
                    
                    # start a new game if 'Enter' is pressed
                    if event.key == pygame.K_RETURN:
                        self.board = [[None for _ in range(3)] for _ in range(3)]
                        self.turn = True
                        self.run_game()

    def is_tie(self) -> bool: pass

    def tie_screen(self) -> None: pass

    def run_game(self) -> None:
        '''
        Main function that runs the tic-tac-toe game.

        Parameters: None

        Returns: None
        '''
        self.draw_grid()
        while True:
            for event in pygame.event.get():
                # if application is closed, quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                # if Q is pressed, quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit(0)
                # if the mouse is clicked...
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get coordinates of the click
                    x, y = pygame.mouse.get_pos()

                    # if click inside grid
                    if self.w // 4 <= x <= self.w * 3 // 4 and self.h // 4 <= y <= self.h * 3 // 4:
                        # get coordinates in grid from click
                        coords = self.calculate_coordinates(x, y, self.w, self.h)

                        # if that square isn't already occupied, draw the necessary shape.
                        if not self.board[coords[0]][coords[1]]: self.draw_xo(coords)
            
            if self.is_win(self.board): self.win_screen()
            elif self.is_tie(): self.tie_screen()

if __name__ == '__main__':
    assert False, f'\n\nThis is a class file and its contents are meant to be imported into another file.\n'
