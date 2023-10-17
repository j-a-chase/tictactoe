######################################################################################################################################################
# Name: James A. Chase
# File: main.py
# Date: 16 October 2023
# Description:
#
# Main file for running tic-tac-toe.
#
######################################################################################################################################################

# imports
from engine import Engine

def main() -> None:
    '''
    Main Function

    Parameters: None

    Returns: None
    '''
    # default to computer being active
    computer = True

    # loop until valid input is given
    while True:
        try:
            player_mode = int(input('One or two players? [1 / 2]: '))
        except ValueError:
            player_mode = 0
        if player_mode == 1 or player_mode == 2: break
    
    # set computer to False if 2-player is selected
    if player_mode == 2: computer = False
    Engine(comp=computer)

# run program
if __name__ == '__main__': main()
