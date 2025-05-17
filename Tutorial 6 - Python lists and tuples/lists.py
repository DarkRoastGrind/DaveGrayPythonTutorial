import os

os.system('clear')

# ------------------------------LIST CREATION-----------------------------
print('------------------------------LIST CREATION-----------------------------')
# Create a list of users, fill it with 3 users. 
users = ['Nicholas','John','Sara']

# Create an array/list, fill it with a str, int, and bool.
data = ['Nicholas',42, True]

# Create an empty list. 
empty_list = []

nums = [4, 42, 78, 1, 5]
print('Lists users, data, empty_list, and nums created.\n')

print('Users list contains:')
print(users)
print()

print('Data list contains:')
print(data)
print()

print('empty_list contains:')
print(empty_list)
print()

print('nums contains:')
print(nums)
print()

# ------------------------------LIST LOGIC-----------------------------
def list_logic(users):
    print('------------------------------LIST LOGIC-----------------------------')
    # Checks is Nicholas is in the users array.
    user = "Nicholas"

    print('Checking if ' + user + ' is within the users list...')
    print(user in users)
    print()

    # Checks is Nicholas is in the data array.
    print('Checking if ' + user + ' is within the data list...')
    print(user in data)
    print()

    # Checks is Nicholas is in the data array.
    print('Checking if ' + user + ' is within the empty_list list...')
    print(user in empty_list)
    print()

    print()

# ------------------------------LIST PRINTING-----------------------------
def list_printing(users):
    print('------------------------------LIST PRINTING-----------------------------')

    # Prints the user in the 0 index position of the users variable. 
    print("User at position 0 in the users list is: " + users[0])

    # Print the last value of our given list. 
    print("User at position -1 in the users list is: " + users[-1])

    # Print the second to last value of our given list. 
    print("User at position -2 in the users list is: " + users[-2])

    # Print the index position of the input item. 
    print("The index value of user sara is: " + str(users.index('Sara')))

    # Print the range of data in the array that includes 0, but not 2. 
    print("The users in the range of 0 to 2 (non-inclusive) are: " + str(users[0:2]))

    # Print the list from the first position, to the end including the final value.
    print("The users in the list start from index 1 are: " + str(users[1:]))

    # Print from the -3 to -1 position, not including the second number. 
    # Same as using 0:2.
    print("The users from range -3 to -1 (non-inclusive) are: " + str(users[-3:-1]))

    # Return the length of the input list. 
    print("The length of the users list is: " + str(len(users)))

    print()

# -----------------------------LIST MODIFICATION - ADDING DATA-----------------------------
def list_adding(users):
    print('--------------------------LIST MODIFICATION - ADDING/MODIFYING DATA--------------------------')
    
    print('Modifying list by adding/replacing, using the list_adding function...')
    users.append('Elsa')
    users += ['Jason']
    users.extend(['Robert','Jimmy'])
    users.insert(0, 'Bob')
    users[2:2] = ['Eddie', 'Alex']
    users[1:3] = ['Robert', 'Jesus']
    print('Modifications complete.')
    print()
    
    # # Add Else to the users list.
    # print ('Adding user else to the users list...')
    # users.append('Elsa')
    # print('The new users list is: ')
    # print(users)
    # print()

    # # Concat two lists, or add the lists together. 
    # # Doing this without using a list, it inserts all individual letters from jasons name.
    # # Jason's name is considered a list of characters. 
    # print ('Combing the list with jason to the users list...')
    # users += ['Jason']
    # print('The new users list is: ')
    # print(users)
    # print()

    # # Extend the users list with the list containing robert and jimmy.
    # print ('Extending the users list with a list containing Robert and Jimmy...')
    # users.extend(['Robert','Jimmy'])
    # print('The new users list is: ')
    # print(users)
    # print()

    # # # Extend the users list using the pre-existing data list. 
    # # print('Extending the users list with the pre-existing data list.')
    # # users.extend(data)
    # # print(users)
    # # print()

    # # Insert a value into the index position of the list.
    # print('Inserting bob into the first index position of the users list...')
    # users.insert(0, 'Bob')
    # print (users)
    # print()

    # # Insert using bracket notation at position 2:2
    # print ('Inserting eddie and alex at position 2:2, pushing all values to the right...')
    # users[2:2] = ['Eddie', 'Alex']
    # print(users)
    # print()

    # # Replace range 1:3 with values. NON-INCLUSIVE. Referred to as a "slice"
    # print ('Replacing range 1:3 with Robert and Jesus.')
    # users[1:3] = ['Robert', 'Jesus']
    # print(users)
    # print()

# -----------------------------LIST MODIFICATION - REMOVING DATA-----------------------------
def list_removing(users):
    print('-----------------------------LIST MODIFICATION - REMOVING DATA-----------------------------')
    print('Modifying the list by removing, using the list_removing function...')
    users.remove('Bob')
    print(users.pop())
    del users[0]
    data.clear()
    print('Modification complete.')
    

    # print('Starting with the current list of users: ')
    # print(users)
    # print()

    # # Remove bob using .remove function.
    # print('Removing Bob from the users list.')
    # users.remove('Bob')
    # print(users)
    # print()

    # # Using POP to remove the last item from the given list, and will return it. 
    # print('Popping the last value from the list.')
    # print(users.pop())
    # print(users)
    # print()

    # # Delete a specific item/index in a list
    # print ('Deleting item at index 0 in the users list...')
    # del users[0]
    # print(users)
    # print()

    # # Deleting the data list completely. 
    # # print ('Deleting the data list completely...')
    # # del data
    # # print ('Data list deleted.')
    # # print()

    # # Clearing the data list.
    # print('Clearing the data list...')
    # data.clear()
    # print('Data cleared, and is now: ')
    # print(data)
    print()

# -----------------------------LIST MODIFICATION - Sorting a list-----------------------------
def list_sorting(users):
    print('-----------------------------LIST MODIFICATION - Sorting a list-----------------------------')

    # Sort the users list alphabetically. 
    print('Sorting the users list alphabetically...')
    users.sort()
    print(users)
    print()
    
    # Replace else with whatever is inserted. 
    print('Replacing the data at 1:2 with nicholas and sorting...')
    users[1:2] = ['nicholas']
    users.sort()
    print(users)
    print()
    
    # Replace else with whatever is inserted. 
    print('Sorting users data compensating for lowercase letters...')
    users.sort(key=str.lower)
    print(users)
    print()

def numlist(nums):
    print('-----------------------------numslist - Reverse sorting-----------------------------')
    # Create a copy of nums to modify within the function.
    # 3 separate ways.
    tempnums = nums.copy()
    mynums = list(nums)
    mynumscopy = nums[:]
    
    print('Testing list copying: ')
    print(tempnums)
    print(mynums)
    print(mynumscopy)
    print()
    
    print('Reversing the tempnums list...')
    tempnums.reverse()
    print(tempnums)
    print()
    
    print('Sorting the tempnums listy in ascending order...')
    tempnums.sort()
    print(tempnums)
    print()
    
    print('Sorting the tempnums list in descending order...')
    tempnums.sort(reverse = True)
    print(tempnums)
    print()
    
# -----------------------------MAIN-----------------------------
print('-----------------------------MAIN-----------------------------')
print('This is the main portion of the program.')
print()

# list_adding(users)
# list_removing(users)
# list_sorting(users)

# numlist(nums)
# print('Original list is kept in-tact using a temporary nums list: ')
# print(nums)
# print()


# print('Checking type of nums list...')
# print(type(nums))
# print()

# -----------------------------Tuples-----------------------------
# Tuple created with constructor
mytuple = tuple(('Nicholas',42,True))

# Another tuple
anothertuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# -----------------------------Packing a tuple-----------------------------
# tuples cannot be changed, but can be copied.
# Create a new list and populate it with mytuple data. 
newlist = list(mytuple)
# Modify the list.

newlist.append('Neil')

# Create a new tuple using the list data.
newtupple = tuple(newlist)

print(newtupple)
print()

# -----------------------------Unpacking a tuple-----------------------------

# Unpack the tuple into the 3 variables. 
# One receives the first, two receives the second, and *hey receives the rest of the data. 
# does not have to be last one, the asterisk can be on any of the variables. 
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

