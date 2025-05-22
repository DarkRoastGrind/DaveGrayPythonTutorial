# Built-in exceptions in python:
# https://www.w3schools.com/python/python_ref_exceptions.asp

# In python, exceptions are raised instead of thrown.
# x is undefined, and will output an error.
# The try except will allow the program to continue.

# COMMENTED OUT TO PREVENT YELLOW WARNINGS IN IDE
# # --------------------undefined variable NameError--------------------
# print("\nTesting NameError using an undefined variable...")
# try:
#     print(x)
# except NameError:
#     print('NameError: Something is probably undefined, fucker.\n')

# --------------------Arithmetic error handling. x/0 is bad error.--------------------
print("\nTesting ZeroDivisionError by dividing x by 0...")
x = 2
try:
    print(x/0)
except ZeroDivisionError:
    print('ZeroDivisionError: Do not divide by zero, fucker.\n')

# --------------------Testing the else and finally blocks..--------------------
print("\nTesting the else and finally blocks for try except using x/1...")
x = 2
try:
    print(f"{x} divided by 1 is: {x/1}")
except ZeroDivisionError:
    print('ZeroDivisionError: Do not divide by zero, fucker.')
else:
    print('No Errors!')
finally:
    print("I'm going to print with or without an error, lil' bitch.\n")

# --------------------Arithmetic error handling. x/0 is bad error.--------------------
print("\nTesting built-in error handling function TypeError by testing if the input is a string...")
x = 2
try:
    if not type(x) is str:
        raise TypeError("Only strings are allowed, fucker.\n")
except NameError:
    print('NameError: Something is probably undefined, fucker.')
except ZeroDivisionError:
    print('ZeroDivisionError: Do not divide by zero, fucker.')
except Exception as error:
    print(error)
else:
    print('\nNo Errors!')


# --------------------Custom Exception Creation.--------------------
class JustNotCoolError(Exception):
    pass


print("\nTesting custom exception creation...")
x = 2
try:
    raise JustNotCoolError("This is a custom exception...Fucker")
except NameError:
    print('NameError: Something is probably undefined, fucker.')
except ZeroDivisionError:
    print('ZeroDivisionError: Do not divide by zero, fucker.')
except Exception as error:
    print(error)
else:
    print('\nNo Errors!')
