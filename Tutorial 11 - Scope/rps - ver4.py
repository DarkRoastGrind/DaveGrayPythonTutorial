import sys
import random
from enum import Enum

# Global variable for counting how many games have been won/lost/tied.
game_count = 0


def play_rps():
    # Create a class to hold the choice variables.
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # Get user input.
    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n")

    # Incorrect input handling.
    if playerchoice not in ["1", "2", "3"]:
        print("\nIncorrect input, please input a choice from 1 to 3!")
        return play_rps()

    # Casting the choice to an int for error handling.
    player = int(playerchoice)

    # Get the computer choice.
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    # output choices.
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("\nThe computer chose " + str(RPS(computer)).replace('RPS.', '') + ".")

    # Game logic function.
    def decide_winner(player, computer):
        def player_win_message():
            print(
                "\n====================="
                "\n     Player wins!    "
                "\n====================="
            )

        def computer_win_message():
            print(
                "\n_._._._._._._._._._._"
                "\n    Python wins!     "
                "\n_._._._._._._._._._._"
            )

        def tie_message():
            print(
                "\n====================="
                "\n        Draw!        "
                "\n====================="
            )

        # Game logic to determine which player won.
        if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
            return player_win_message()
        elif player == computer:
            return tie_message()
        else:
            return computer_win_message()

    # Call the game logic function.
    decide_winner(playerchoice, computerchoice)

    # Using the global game_count variable.
    global game_count

    # Increment how many games have been played.
    game_count += 1

    # Print out how many games have been played.
    print("\nGame Count: " + str(game_count))

    # Ask the user if they want to play the game again.
    print("\nPlay again?")

    # Error checking for user input.
    while True:
        playagain = input("\nY for yes; \nQ to quit.")

        if playagain.lower() not in ["y", "q"]:
            print("\nInvalid input, please input Y for yes, or Q for quit.")
            continue
        else:
            break

    # Decision handling for gameplay loop.
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\nThank you for playing!\n")
        sys.exit("Goodbye!")


play_rps()
