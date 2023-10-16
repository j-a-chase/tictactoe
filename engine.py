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
