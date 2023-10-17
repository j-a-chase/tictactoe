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
from typing import Tuple

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
        
        display.update()

    def calculate_coordinates(self, x: int, y: int, width: int, height: int) -> Tuple:
        '''
        Calculates which grid square the drawing should be placed in depending on what the coordinates provided are.

        Parameters:
            - x: integer containing the x-value for where the mouse was clicked
            - y: integer containing the y-value for where the mouse was clicked

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
        
        # change who's turn it is and update display
        self.turn = not self.turn
        display.update()
        

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

                    # if coordinates are outside of the grid, ignore
                    if x < 150 or x > 450 or y < 150 or y > 450: continue

                    # get coordinates in grid from click
                    coords = self.calculate_coordinates(x, y, self.w, self.h)

                    # if that square isn't already occupied, draw the necessary shape.
                    if not self.board[coords[0]][coords[1]]: self.draw_xo(coords)

if __name__ == '__main__':
    assert False, f'\n\nThis is a class file and its contents are meant to be imported into another file.\n'
