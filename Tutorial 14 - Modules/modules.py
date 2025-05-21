# PYTHON STANDARD LIBRARY: https://docs.python.org/3/library/index.html
# PYTHON MODULE LIBRARY: https://docs.python.org/3/py-modindex.html

# Modules are code libraries, allowing you to use
# functions from other files.

# Import the math module.
import math

# Import the system module to handle system commands
# such as exiting the program.
import sys

# Import the random module for random input/output.
# Create an alias, rdm, to use instead of the entire
# file name of random.
import random as rdm

# Import a specific function/item from a module
from enum import Enum

# Import pi in specific.
from math import pi

# Import the custom kansas module
import kansas

# Import the rock_paper_scissors functions.
from rps_ver7 import rock_paper_scissors

# Print the capital of kansas, and a random fun fact.
print(f"\nThe capital of Kansas is: {kansas.capital}")
kansas.randomfunfact()

# Print the name of the current running module.
print()  # New line
print(__name__)
print(kansas.__name__)

# Start rock paper scissors.
rock_paper_scissors()

# # Print pi using the math notation.
# print(math.pi)

# # Print pi using the imported pi method.
# print(pi)

# # Output a random number from the given string.
# rdm.choice(("123"))

# # This will print each item in the random directory.
# for item in dir(rdm):
#     print(item)

# Exit the program
sys.exit()
