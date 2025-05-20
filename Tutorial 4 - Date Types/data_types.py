# import math module. 
import math

# String data type

#--------------------------------Literal Assignment--------------------------------
# literal assignment
first = "Nicholas"
last = "La Claire"

# Print out the type of first.
print (type(first))

# Is the type of first str?
print (type(first) == str)

# Is the instance of first a string?
print (isinstance(first, str))

#--------------------------------Constructor function--------------------------------
# constructor function
pizza = str("Pepperoni")

# Print out the type of first.
print (type(pizza))

# Is the type of first str?
print (type(pizza) == str)

# Is the instance of first a string?
print (isinstance(pizza, str))

#--------------------------------Concatenation--------------------------------
# First and last name concatenated into fullname.
fullname = first + " " + last
print (fullname)

# ! is added to full name.
fullname += "!"
print (fullname)

#--------------------------------Casting a number to a string--------------------------------
# 1980 is now cast to a string.
decade = str(1980)

print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

#--------------------------------Multiple lines--------------------------------
multiline = '''
Hey, how are you?               

I was just checking in.         

                                All good?

'''
print(multiline)

#--------------------------------Escaping special characters--------------------------------
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#--------------------------------String Methods--------------------------------
print(first)

# Won't change value, will just return lowercase.
print(first.lower())

# Return uppercase.
print(first.upper())

#Return normal.
print(first)

# Turn's everything to propercase, capitalizing first letters for all words..
print(multiline.title())

# Print, but replace any instance of good with ok.
print(multiline.replace("good", "ok"))

# Print for comparison.
print(multiline)

# Show original length of multiline. 
print(len(multiline))

# Add random characters
multiline += "                                                                   "
multiline = "                                                                   " + multiline

# Show changed length of multiline.  
print(len(multiline))

# Remove white spaces, but will jumble all words together. 
print(len(multiline.strip()))

# Remove white space from left side.
print(len(multiline.lstrip()))

# Remove white space from right side. 
print(len(multiline.rstrip()))

print ("")

# Build a menu
title = "menu".upper()
# Center the title within the = character.
print(title.center(20, "="))

print("Coffee".ljust(16,".")+ "$1".rjust(4))
print("Muffin".ljust(16,".")+ "$2".rjust(4))
print("Cheesecake".ljust(16,".")+ "$4".rjust(4))

print ("")

#--------------------------------String Index Values--------------------------------
# Print the value at index 1, or the second letter of the first name string 
print(first[1])

# Print the last letter of the string.
print(first[-1])

# Print the first letter of the string.
print(first[0])

# Print a range from 0 to -1, but will not print the value at -1. 
print(first[0:-1])

# Print a range from 0 to the end of the string.
print(first[0:])

print ("")

#--------------------------------Some methods that return boolean data.--------------------------------
# Does the string start with a N?
print(first.startswith("N"))

# Does the string end with a Z?
print(first.endswith("Z"))

print ("")

#--------------------------------Boolean data type--------------------------------
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))
print ("")

#--------------------------------Numeric data type--------------------------------
# integer
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))
print ("")

# Float
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))
print ("")

# complex type - Electrical engineering
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print ("")

#--------------------------------Built-in functions for numbers--------------------------------
print(abs(gpa))

print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

print ("")

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print ("")

#--------------------------------CAsting string to number--------------------------------
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
print ("")

#error if you attempt to cast incorrect data. 
# zip_value = int("New York")