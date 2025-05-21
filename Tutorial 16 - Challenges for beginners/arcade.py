import sys
from rps_ver9 import rps
from guess_number import gng


def arcade(name='PlayerOne'):
    welcome_back = False
    game_choice = 0

    def choose_game():
        nonlocal welcome_back
        nonlocal name
        nonlocal game_choice

        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade!")

        game_choice = input(
            f"Please choose a game:\n1 for Rock Paper Scissors\n2 for Guess My number\n\nOr press \"x\" to exit the arcade.\n"
        )

        if game_choice not in ["1", "2", "x"]:
            print(
                f"\n{name}, incorrect input, please chose a game or press x to exit!")
            return choose_game()

        welcome_back = True

        if (game_choice == "x"):
            print("\nThank you for using the arcade!\n")
            sys.exit(f"Goodbye {name}!")

        choice = int(game_choice)

        if (choice == 1):
            rock_paper_scissors = rps(name)
            rock_paper_scissors()

        elif (choice == 2):
            guess_my_number = gng(name)
            guess_my_number()

        print(f"\nPlay another game, {name}?")

        while True:
            playagain = input("\nY for yes; \nQ to quit.")

            if playagain.lower() not in ["y", "q"]:
                print("\nInvalid input, please input Y for yes, or Q for quit.")
                continue
            else:
                break

        if playagain.lower() == "y":
            return choose_game()
        else:
            print("\nThank you for using the arcade!\n")
            sys.exit(f"Goodbye {name}!")

    return choose_game


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
    print(f"\n{args.name}, welcome to the arcade!")

    choose_game = arcade(args.name)
    choose_game()
