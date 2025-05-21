# Global scope variable.
name = "Nicholas"
count = 1

# Function accessing global variable.
def greeting ():
    # With no variables in the parameters defined, print(name) will print our global name.
    print(name)

greeting()

# Function with only local variable
def greeting():
    # This variable is only local to this function. It cannot be used outside
    # Unless the variable is returned using return color
    color = "blue"
    return 0

# Function using parameter
def greeting(firstname):
    print(name)
    print(firstname)
    return 0

# Passing a first name as a string to the function
greeting("George")

# Using a parameter that is the same name as the global variable. 
def greeting(name):
    print(name)
    return 0

# Passing a first name as a string to the function. 
# The global variable will not be printed. 
greeting("George")

# Creating a function that calls the global function, greeting. 
def global_function():
    greeting("Nicholas")

global_function()

# Defining a function within a function. 
def global_function_create():
    def greeting2(name):
        print(name)

# Defining a function within a function, adding a variable in the parent function.
def global_function_variable():
    color = "blue"
    
    # If this function would only be useful in the parent function, only use it in the parent. 
    # Polluting the global scope exists. 
    def greeting2(name):
        print(color)
        print(name)
    
    greeting2("Nicholas")

global_function_variable()

# Define the variable to be used within the function as the global variable.
# You can then modify that variable. 
def modify_global_variable():
    # Find the global variable count
    global count
    
    # Add 1 to it.
    count += 1
    
    print(count)

modify_global_variable()

def non_global_variable():
    color = "Blue"
    global count
    # Specifically designate the variable as a non global, or as a local variable. 
    # This forces the function to use the parent variable. 
    def non_global():
        nonlocal color
        color = "red"
        print(color)
        
    non_global()
    print(color)

non_global_variable()