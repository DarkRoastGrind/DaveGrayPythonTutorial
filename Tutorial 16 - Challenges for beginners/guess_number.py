import sys
import random
from enum import Enum


def gng(name='PlayerOne'):
    player_choice = 0
    player_wins = 0
    computer_wins = 0
    game_count = 0

    def play_gng():
        nonlocal name
        nonlocal player_choice
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal game_count

        computer_number = random.choice("123")
        computer = int(computer_number)

        def game_counts():
            print(
                f"\nGame Count: {game_count}\n{name}'s Wins: {player_wins}\nComputer Wins: {computer_wins}\n{name}'s winning Percentage: {player_wins/game_count:.2%}"
            )

        def input_feedback():
            print(
                f"\n{name}, you chose {player_choice}.\nI was thinking {computer_number}."
            )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal game_count

            def player_win_message():
                print(
                    f"\n{name}, you win!"
                )

            def computer_win_message():
                print(
                    f"\nI won! Sorry {name}!"
                )

            game_count += 1

            if (player == computer):
                player_wins += 1
                return player_win_message()

            else:
                computer_wins += 1
                return computer_win_message()

        player_choice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n"
        )
        if player_choice not in ["1", "2", "3"]:
            print(f"\n{name}, incorrect input, please input a choice from 1 to 3!")
            return play_gng()
        player = int(player_choice)

        input_feedback()
        decide_winner(player, computer)
        game_counts()

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for yes; \nQ to quit.")

            if playagain.lower() not in ["y", "q"]:
                print(
                    "\nInvalid input, please input Y for yes, or Q for quit."
                )
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gng()
        else:
            print("\nThank you for playing!\n")
            sys.exit(f"Goodbye {name}!")

    return play_gng


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
    guess_number_game = gng(args.name)
    guess_number_game()
