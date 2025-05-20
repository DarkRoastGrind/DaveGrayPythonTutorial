import sys
import random
from enum import Enum

# Create a class to hold the choice variables. 
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Variable used to loop the game.
playagain = True

while playagain:
    # Ways to get the values/returns from the above class. 
    # print (RPS(2))
    # print (RPS.ROCK)
    # print (RPS['ROCK'])
    # print (RPS.ROCK.value)
    # sys.exit()

    # Get user input.
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

    # Casting the choice to an int for error handling.
    player = int(playerchoice)

    # Handle incorrect input. CHANGED TO OR FROM | IN TUTORIAL 6
    if player < 1 or player > 3:
        sys.exit("Incorrect input, please input 1, 2, or 3.")

    # Get the computer choice.
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    # output choices. 
    print("\nYou chose " + str(RPS(player)).replace('RPS.','') + ".")
    print("The computer chose " + str(RPS(computer)).replace('RPS.','') + ".\n")

    # Game logic
    if player == 1 and computer == 3:
        print("Player wins!")
        
    elif player == 2 and computer == 1:
        print("Player wins!")
        
    elif player == 3 and computer == 2:
        print("Player wins!")

    elif player == computer:
        print("Draw!")

    else:
        print("Python wins!")
    
    playagain = input("\nPlay again? \n Y/N \n Q to quit.\n\n")
    
    if playagain.lower() == "y":
        continue
    else:
        print("\nThank you for playing!\n")
        break
    
sys.exit("Goodbye!")

