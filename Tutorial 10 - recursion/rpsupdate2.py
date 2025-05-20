import sys
import random
from enum import Enum

def play_rps():
    # Create a class to hold the choice variables. 
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    
    # Get user input.
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n")
    
    # Incorrect input handling. 
    if playerchoice not in ["1","2","3"]:
        print("\nIncorrect input, please input a choice from 1 to 3!")
        return play_rps()
    
    # Casting the choice to an int for error handling.
    player = int(playerchoice)
        
    # Get the computer choice.
    computerchoice = random.choice("123")
    
    computer = int(computerchoice)
    
    # output choices. 
    print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("\nThe computer chose " + str(RPS(computer)).replace('RPS.','') + ".")
    
    # Game logic
    if player == 1 and computer == 3:
        print("\n=====================")
        print("\n     Player wins!    ")
        print("\n=====================")
        
    elif player == 2 and computer == 1:
        print("\n=====================")
        print("\n     Player wins!    ")
        print("\n=====================")
        
    elif player == 3 and computer == 2:
        print("\n=====================")
        print("\n     Player wins!    ")
        print("\n=====================")
        
    elif player == computer:
        print("\n=====================")
        print("\n        Draw!        ")
        print("\n=====================")
        
    else:
        print("\n_._._._._._._._._._._")
        print("\n    Python wins!     ")
        print("\n_._._._._._._._._._._")
        
    print ("\nPlay again?")
    
    while True:
        playagain = input("\nY for yes; \nQ to quit.")
        
        if playagain.lower() not in ["y", "q"]:
            print("\nInvalid input, please input Y for yes, or Q for quit.")
            continue
        else:
            break
        
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\nThank you for playing!\n")
        sys.exit("Goodbye!")

play_rps()
