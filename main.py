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
from inputs import multiplayer, difficulty

def main() -> None:
    '''
    Main Function

    Parameters: None

    Returns: None
    '''
    # determine if the game is multiplayer or not
    computer_player = not multiplayer()

    # start game
    if computer_player: Engine(comp = computer_player, difficulty = difficulty())
    else: Engine(comp = computer_player)

# run program
if __name__ == '__main__': main()
