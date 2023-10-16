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
from typing import List

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
        self.width = width
        self.height = height
        
        # internal representation of game board
        self.board = [[None for x in range(3)] for y in range(3)]

        # initialize display assets
        self.window = display.set_mode((width, height))
        display.set_caption('Tic-Tac-Toe')

        # initialize fonts
        self.text_font = pygame.font.SysFont('timesnewroman', 15)

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
                            (self.width * 3 // 12, self.height * 5 // 12),
                            (self.width * 9 // 12, self.height * 5 // 12), 7)
        pygame.draw.line(self.window, self.BOARD_COLOR,
                            (self.width * 3 // 12, self.height * 7 // 12),
                            (self.width * 9 // 12, self.height * 7 // 12), 7)
        pygame.draw.line(self.window, self.BOARD_COLOR,
                            (self.width * 5 // 12, self.height * 3 // 12),
                            (self.width * 5 // 12, self.height * 9 // 12), 7)
        pygame.draw.line(self.window, self.BOARD_COLOR,
                            (self.width * 7 // 12, self.height * 3 // 12),
                            (self.width * 7 // 12, self.height * 9 // 12), 7)
        
        display.update()

    def run_game(self) -> None:
        self.draw_grid()
        while True:
            for event in pygame.event.get():
                # if application is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit(0)
