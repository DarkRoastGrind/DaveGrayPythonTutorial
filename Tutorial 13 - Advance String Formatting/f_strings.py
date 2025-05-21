# String example
person = "Nicholas"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")

# Other ways to format strings
# This inserts the individual variables into their correct locations
message = "\n%s has %s coins left." % (person, coins)
print(message)

# Format message method. If brackets are not filled,
# Messages will be filled from first to last.
message = "\n{} has {} coins left.".format(person, coins)
print(message)

# Format message method using index methods. Coins and person flipped.
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

# Format message method. Assign using name, and assign values in the methods.
message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person)
print(message)

# Format message method, using a dictionary.
player = {"person": "Nicholas", "coins": 3}
# Pulls values in from the player dictionary.
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

# --------------------------------------------------------#
# f-strings.

# Insert global variables directly into the string.
message = f"\n{person} has {coins} coins left."
print(message)


# Showing that you can use anything within these braces.
message = f"\n{person} has {2*5} coins left."
print(message)
message = f"\n{person.lower()} has {2*5} coins left."
print(message)

# Using a dictionary with the message.
message = f"\n{player['person']} has {coins} coins left."
print(message)

# Passing options into f-strings.
num = 10
# The .2f indicates decimal spaces, fixed.
print(f"\n2.25 times {num} is {2.25*num:.2f}\n")

# Using the formatting in a loop.
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25*num:.2f}")
print()

# Using the formatting in a loop, using a percent output.
for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num/4.52:.2%}")
print()

# Formatting options for strings can be found here:
# https://www.w3schools.com/python/ref_string_format.asp
