######################################################################################################################################################
# Name: James A. Chase
# File: inputs.py
# Date: 24 October 2023
# Description:
#
# Module for functions handling input from the user prior to game starting.
#
######################################################################################################################################################

def multiplayer() -> bool:
    '''
    Gets information from the user on the number of players playing the game.

    Parameters: None

    Returns:
        - A boolean indicating if it is a multiplayer game or not.
    '''
    # loop until valid input is given
    while True:

        # account for user inputting something invalid
        try:
            # get user input and convert to int
            multiplayer = int(input('One or two players? [1 / 2]: '))

            # handle all invalid inputs the same
            if multiplayer < 1: raise ValueError
            
            multiplayer -= 1 # single-player == 0 (False), multiplayer >= 1 (True)
            return multiplayer
        # handle invalid input
        except ValueError: print('Invalid input!')

def difficulty() -> int:
    '''
    Gets information from the user regarding their desired CPU player difficulty.

    Parameters: None

    Returns:
        - an integer indicating the difficulty of the CPU game.
    '''
    # loop until valid input is given
    while True:
        # account for invalidity from user
        try:
            # get difficulty
            dif = int(input('Easy, Medium, or Hard difficulty? [0 / 1 / 2]: '))

            # if its negative, throw error to handle all invalid input the same way
            if dif < 0: raise ValueError

            # return difficulty value (0: Easy, 1: Medium, >= 2: Hard)
            return dif
        except ValueError: print('Invalid input!')

if __name__ == '__main__': assert False, 'This is a module. Please import its contents into another file.'
