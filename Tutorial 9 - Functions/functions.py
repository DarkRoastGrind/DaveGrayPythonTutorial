# Simple hello world function
def hello_world():
    print("Hello world!")

# Call the function
hello_world()

# Simple arithmetic function
def sum(x, y):
    print(x + y)

# Use the sum function with 4 and 8. 
sum(4, 8)

# Simple arithmetic function, but only returns the value for the program to use. 
def sum2(x, y):
    return x + y

# Call sum2 to add 2 and 3, allocate the product into total, print total. 
total = sum2(2, 3)
print(total)

# type checks for x and y to ensure ints. If not ints, returns. 
def sum3(x, y):
    if(type(x) is not int or type(y) is not int):
        return
    return x + y

# Returns none. Indicates an incorrect input. 
total = sum3("A", 3)
print(total)

# Default parameters/construction 
def sum4(x, y=3):
    if(type(x) is not int or type(y) is not int):
        return
    return x + y

# Will add 1 to the default constructed y value of 3. 
total = sum4(1)
print(total)

# Default parameters/construction for both values.
def sum5(x=0, y=0):
    if(type(x) is not int or type(y) is not int):
        return
    return x + y

# return the default values of 0 and 0.
total = sum5()
print(total)

# Default parameters/construction for both values. Added 0 to return, as a default return.
def sum6(x=0, y=0):
    if(type(x) is not int or type(y) is not int):
        return 0
    return x + y

# return only 0.
total = sum6()
print(total)

# Functions with multiple unknown arguments
# Asterisk causes data to become a tuple. 
def multiple_items(*args):
    print(args)
    print(type(args))

# Output the args and type. 
multiple_items("Nick", "John", "Sara", 1, 2, 3)

# Keyword arguments
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

# Output the kwargs and type. Requires naming, as shown. 
mult_named_items(first = "Nick", last = "LaClaire")
# output: 
# {'first': 'Nick', 'last': 'LaClaire'}
# <class 'dict'>

