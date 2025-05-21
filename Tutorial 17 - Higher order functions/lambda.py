# Lambda function is a single expression that returns a value.

# This function simply squares a number and returns it's value.
# Cannot be called by name, but can be assigned to a variable.


# squared = lambda num: num * num
from functools import reduce
def squared(num): return num * num


print(squared(2))


# Add two numbers
# addtwo = lambda num: num+2
def addtwo(num): return num+2


print(addtwo(12))


# Simple addition function.
# sum = lambda a, b: a+b
def sum_total(a, b): return a+b


print(sum_total(2, 2))


# ---------------------------------------------------------#
# Lambdas mostly use inside other functions as a quick function.

# Simple function
def funcbuilder(x):
    return lambda num: num+x


# Create other functions easily.
addten = funcbuilder(10)
addtwenty = funcbuilder(20)


print(addten(7))
print(addtwenty(7))

# ---------------------------------------------------------#
# Higher order functions - Map

numbers = [3, 7, 12, 18, 20, 21]

# Map receives a function as the first argument.
# This will iterate over each item in the numbers list and
# will apply the function to it. It will then create a new
# list containing the numbers.
squared_nums = map(lambda num: num*num, numbers)

print(list(squared_nums))

# ---------------------------------------------------------#
# Higher order functions - Filter

# Return true if 1, false if 0.
odd_nums = filter(lambda num: num % 2 != 0, numbers)

# Return only the odd numbers, or the numbers that have the true result.
print(list(odd_nums))

# ---------------------------------------------------------#
# Higher order functions - reduce
numbers = [1, 2, 3, 4, 5, 1]

# Adds all numbers together. Starting value is set at the end as 10.
total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

# Much simpler than using reduce.
# Avoid reduce if there is a simpler solution
print(sum(numbers, 10))

# ---------------------------------------------------------#
# Higher order functions - reduce - Complex solution
names = ['Nicholas', 'sara ito', 'John Jacob Jingleheimerschmidt']

# Add all characters in the strings in the names list.
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
