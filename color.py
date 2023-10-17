######################################################################################################################################################
# Name: James A. Chase
# File: color.py
# Date: 5 October 2023
######################################################################################################################################################

# imports
from typing import Tuple
from random import randint

def get_color(color: str) -> Tuple[int, int, int]:
    '''
    Returns the RGB values for the given color.

    Parameters:
        - color: a string containing the name of a color

    Returns:
        - A tuple containing the RGB values for the color provided.
    '''
    # a dictionary containing the known colors
    known_colors = {
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255),
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'ORANGE': (255, 165, 0),
        'DARKGREY': (50, 50, 50)
    }

    # force input to uppercase
    color = color.upper()
    
    # check if the color is in the dictionary, else return invalid value
    return known_colors[color] if color in known_colors else (-1, -1, -1)

def get_random_color() -> Tuple[int, int, int]:
    '''
    Generates a random color.

    Parameters: None

    Returns:
        - A tuple containing randomly generated RGB values
    '''
    # generate three random integers between 0 - 255 and return the resulting tuple
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def convert_from_hex_string(color: str) -> Tuple[int, int, int]:
    '''
    Converts a hexadecimal color (ex: FFFFFF) to its corresponding RGB values (ex: 255, 255, 255)

    Parameters:
        - color: a string representing a hexadecimal number

    Returns:
        - A tuple containing the given color in RGB values
    '''
    # parse every pair of hexadecimal digits and return the resulting tuple
    return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)

if __name__ == '__main__': assert False, '\n\nThis is a module, please import its contents into another file.\n'