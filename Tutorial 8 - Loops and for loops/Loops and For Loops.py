# While loops

# value = 1
# while value < 10:
#     print(value)
#     # when value = 5, stop. 
#     if value == 5:
#         break
#     value += 1

# Continue function
# value = 1
# while value < 10:
#     value += 1
#     # when value = 5, stop. 
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# Lists using for loops
names = ["Nick", "Sara", "John"]

# # Can use anything in place of x. This will print all 3 names after each other. 
# for x in names:
#     print(x)

# # this will print each individual letter in mississippi
# for x in "Misssissippi":
#     print(x)

# When x = sara, the loop stops, and only Nick is returned. 
# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# # Starting at index of 0, we print x up to 3.
# for x in range(4):
#     print(x)

# # Start at index 2, end at index 4. 
# for x in range(2, 4):
#     print(x)
    
# # Tell the loop how to increment, or how many numbers to increase/decrease by.
# # Start at index 0, go to 100, increment by 5.  
# for x in range(0, 100, 5):
#     print(x)
# else:
#     print("Glad that\'s Over!")

actions=["codes","eats","sleeps"]

# # Nested for loops. 
# Applies action to each name first. 
# Rotates actions first. 
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

# Applies code to each name before moving to next action. 
# Rotates names first.
for action in actions:
    for name in names:
        print(name + " " + action + ".")