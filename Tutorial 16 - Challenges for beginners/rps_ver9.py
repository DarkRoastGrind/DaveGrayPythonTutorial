# Run the game using py rps_ver8.py -n "Name"
import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    # Parent function variables for counting
    # how many games have been won/lost/tied/played.
    game_count = 0
    player_wins = 0
    computer_wins = 0
    draw_count = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal draw_count
        nonlocal game_count

        # Create a class to hold the choice variables.
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Game logic function.
        def decide_winner(player, computer):
            # Grab parent variables.
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal draw_count

            def player_win_message():
                print(
                    f"\n=====================\n     {name} wins!    \n====================="
                )

            def computer_win_message():
                print(
                    "\n_._._._._._._._._._._"
                    f"\n    Python wins!     \n   Sorry {name}!    "
                    "\n_._._._._._._._._._._"
                )

            def tie_message():
                print(
                    "\n====================="
                    "\n        Draw!        "
                    "\n====================="
                )

            # Game logic to determine which player won.
            if (
                player == 1
                and computer == 3
                or player == 2
                and computer == 1
                or player == 3
                and computer == 2
            ):
                player_wins += 1
                return player_win_message()

            elif player == computer:
                draw_count += 1
                return tie_message()
            else:
                computer_wins += 1
                return computer_win_message()

        # Function for printing out game results.
        def game_counts():
            print(
                f"\nGame Count: {game_count}\n {name}'s Wins: {player_wins}\n Computer Wins: {computer_wins}\n Draws: {draw_count}"
            )

        # Function for returning the input to the player.
        def input_feedback():
            print(
                f"\n{name}, you chose {str(RPS(player)).replace("RPS.", "")}.\nThe computer chose {str(RPS(computer)).replace("RPS.", "")}."
            )

        # Get user input.
        playerchoice = input(
            f"\n{name}, please enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors:\n")

        # Incorrect input handling.
        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, incorrect input, please input a choice from 1 to 3!")
            return play_rps()

        # Casting the choice to an int for error handling.
        player = int(playerchoice)

        # Get the computer choice.
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        # output choices feedback to indicate what each player chose.
        input_feedback()

        # Call the game logic function.
        decide_winner(player, computer)

        # Increment how many games have been played.
        game_count += 1

        # Call function to display game results.
        game_counts()

        # Ask the user if they want to play the game again.
        print(f"\nPlay again, {name}?")

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
            return

    # Return the child function
    return play_rps


# Only execute if this is the currently called file.
if __name__ == "__main__":
    # Part of python standard library.
    # Command line argument and parsing library.
    import argparse

    # Description of the argument parser.
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    # Type py hello_person.py -h for a help message.
    parser.add_argument(
        "-n", "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game."
    )

    args = parser.parse_args()

    # Holds the rps function
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
