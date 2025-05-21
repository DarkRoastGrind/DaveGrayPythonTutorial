# Closure is a function having to access to the scope of its parent
# function after the parent function has returned.


# Nested function for closure example.
def parent_function(person, coins):
    # coins = 3

    def play_game():
        # Grab parent variable
        nonlocal coins

        # Decrement the coins variable.
        coins -= 1

        # Return how many coins are left.
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins remaining")

        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin remaining")

        else:
            print(
                "\n"
                + person
                + " has "
                + str(coins)
                + " coins remaining. Please insert more coins."
            )

    # Return the play_game function to be used outside of the parent function
    return play_game


# Assign the parent function to tommy and jenny, initializing them
# With their respective names, and total coins.
tommy = parent_function("Tommy", 3)
jenny = parent_function("jenny", 5)

# Call the above as functions, essentially indicating the act of
# inserting a coin in order to play the game.
tommy()
tommy()
jenny()
jenny()
tommy()
jenny()
jenny()
tommy()
tommy()
