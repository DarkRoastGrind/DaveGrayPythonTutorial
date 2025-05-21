import sys
import random
from enum import Enum

# Create a class to hold the choice variables. 
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Ways to get the values/returns from the above class. 
# print (RPS(2))
# print (RPS.ROCK)
# print (RPS['ROCK'])
# print (RPS.ROCK.value)
# sys.exit()

# Empty line to separate new game and old game
print("")

# Get user input.
playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")

# Casting the choice to an int for error handling.
player = int(playerchoice)

# Handle incorrect input. CHANGED TO OR FROM | IN TUTORIAL 6
if player < 1 or player > 3:
    sys.exit("Incorrect input, please input 1, 2, or 3.")

# Get the computer choice.
computerchoice = random.choice("123")
computer = int(computerchoice)

# output choices. 
print("")
print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
print("The computer chose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

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
