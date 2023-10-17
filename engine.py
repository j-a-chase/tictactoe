######################################################################################################################################################
# Name: James A. Chase
# File: engine.py
# Date: 16 October 2023
# Description:
#
# File containing the Engine class for running tic-tac-toe.
#
######################################################################################################################################################

# external imports
import pygame
from pygame import display
from typing import Tuple
from win32gui import SetWindowPos

# local imports
import color
from calculations import calculate_coordinates, is_win, is_tie, get_x_coords, get_o_coords, computer_move

class Engine:
    def __init__(self, width: int = 600, height: int = 600, comp=True) -> None:
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
        self.BG_COLOR = color.convert_from_hex_string('FFFFFF')
        self.BOARD_COLOR = color.convert_from_hex_string('000000')
        self.X_COLOR = color.get_random_color()
        self.O_COLOR = color.get_random_color()
        self.TEXT_COLOR = color.get_color('darkgrey')

        # display dimensions
        self.w = width
        self.h = height
        
        # internal representation of game board
        self.board = [[None for x in range(3)] for y in range(3)]

        # initialize display assets
        self.window = display.set_mode((width, height))
        display.set_caption('Tic-Tac-Toe')

        # ensure the pygame window is brought to the front upon completion of the input command in main.py
        SetWindowPos(display.get_wm_info()['window'], -1, display.Info().current_w, display.Info().current_h // 4, 0, 0, 1)

        # initialize fonts
        self.text_font = pygame.font.SysFont('timesnewroman', 15)
        self.turn_font = pygame.font.SysFont('timesnewroman', 25)
        self.victory_font = pygame.font.SysFont('timesnewroman', 40)

        # initialize gameplay variables
        self.turn = True
        self.computer_player = comp

        # start game
        self.run_game()
    
    def __str__(self) -> str:
        '''
        Controls how it is handled when object is converted into a string.

        Parameters: None

        Returns:
            - A string representing the tic-tac-toe grid
        '''
        # organizes the board as a 3x3 list
        s = ''
        for row in self.board:
            s += str(row) + '\n'
        return s
    
    def __repr__(self) -> str:
        '''
        Controls how Engine is represented in a more information-rich format.

        Parameters: None

        Returns:
            - A string explaining the Engine class object
        '''
        # include class information
        return f'{__class__}\n{self.__str__()}'
    
    def clear_screen(self) -> None:
        '''
        Paints the whole screen the color of the background.

        Parameters: None

        Returns: None
        '''
        self.window.fill(self.BG_COLOR)
        display.update()

    def draw_grid(self) -> None:
        '''
        Draws the tic-tac-toe grid on screen.

        Parameters: None

        Returns: None
        '''
        # make sure screen is cleared
        self.clear_screen()

        # draw grid lines
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
        
        # render instruction text
        instruction_text = self.text_font.render('Click to place X or O - Q to quit', 1, self.TEXT_COLOR)
        self.window.blit(instruction_text, (self.w // 3, self.h * 5 // 6))

        # render text indicating whose turn it is
        turn_text = self.turn_font.render('X\'s turn.', 1, self.TEXT_COLOR)
        self.window.blit(turn_text, (self.w * 5 // 12 + (self.w // 60), self.h // 6))
        
        display.update()

    def draw_xo(self, coord: Tuple[int, int]) -> None:
        '''
        Draws an X or O depending on whose turn it is given the coordinates of the click.

        Parameters:
            - coord: Tuple indicating which row and column were clicked

        Returns: None
        '''
        if self.turn: # 'X'
            # get shape coordinates from dictionary holding the necessary coordinate values for drawing an 'X'
            shape = get_x_coords(self.w, self.h)[str(coord)]
            pygame.draw.line(self.window, self.X_COLOR, shape[0], shape[1], 3)
            pygame.draw.line(self.window, self.X_COLOR, shape[2], shape[3], 3)

            # update internal board
            self.board[coord[0]][coord[1]] = 'X'
        else: # 'O'
            # get shape coordinates from dictionary holding the necessary coordinate values for drawing an 'O'
            shape = get_o_coords(self.w, self.h)[str(coord)]
            pygame.draw.ellipse(self.window, self.O_COLOR,
                                pygame.Rect(shape[0], shape[1], self.w // 12, self.h // 12), 3)
            
            # update internal board
            self.board[coord[0]][coord[1]] = 'O'
        
        # update turn text
        self.turn = not self.turn
        symbol = 'X' if self.turn else 'O'
        turn_text = self.turn_font.render(f'{symbol}\'s turn.', 1, self.TEXT_COLOR)
        self.window.fill(self.BG_COLOR, pygame.Rect(self.w * 5 // 12, self.h // 6, self.w // 6, self.h // 24))
        self.window.blit(turn_text, (self.w * 5 // 12 + (self.w // 60), self.h // 6))

        # update display
        display.update()

    def game_over_screen(self, win: bool = False) -> None:
        '''
        Displays the screen for a tie and handles events to continue or quit play.

        Parameters:
            - win: a boolean value indicating if the game was won or not

        Returns: None
        '''
        # clear turn text to replace with victory text
        self.window.fill(self.BG_COLOR, pygame.Rect(self.w * 5 // 12, self.h // 6, self.w // 6, self.h // 24))

        # clear old instruction text to replace with updated instruction text
        self.window.fill(self.BG_COLOR, pygame.Rect(self.w // 3, self.h * 5 // 6, self.w * 5 // 12, self.h // 24))

        # grab correct symbol
        symbol = 'O' if self.turn else 'X'

        # render victory text
        if win:
            victory = self.victory_font.render(f'{symbol}\'s win!', 1, self.TEXT_COLOR)
        else: # must be draw
            victory = self.victory_font.render(f'  Draw!', 1, self.TEXT_COLOR)
        self.window.blit(victory, (self.w * 9 // 24 + (self.w // 60), self.h // 6))

        # render new instruction text
        instruction = self.text_font.render('Press Q to quit - Press \'Enter\' to continue playing', 1, self.TEXT_COLOR)
        self.window.blit(instruction, (self.w // 4, self.h * 5 // 6))

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

    def run_game(self) -> None:
        '''
        Main function that runs the tic-tac-toe game.

        Parameters: None

        Returns: None
        '''
        # draw tic-tac-toe grid
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
                        coords = calculate_coordinates(x, y, self.w, self.h)

                        # if that square isn't already occupied, draw the necessary shape.
                        if not self.board[coords[0]][coords[1]]: self.draw_xo(coords)
            
            # check for a win or tie
            if is_win(self.board): self.game_over_screen(win=True)
            elif is_tie(self.board): self.game_over_screen()

            # if computer play is enabled, perform computer move after human move
            if self.computer_player and not self.turn:
                pygame.time.delay(1000)
                x_y = computer_move(self.board)
                self.draw_xo(x_y)

if __name__ == '__main__': assert False, f'\n\nThis is a class file and its contents are meant to be imported into another file.\n'
