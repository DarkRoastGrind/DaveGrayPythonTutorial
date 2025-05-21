value = True

# Will complete  one loop, then go back around and stop.
while value:
    print(value)
    value = False
print()

# Printing using charaters.
value2 = "y"

# Value is now y. If changed from y, it will exit the loop.
while value2:
    print(value2)
    value2 = False
print()

# Using another argument.
value3 = "y"
count = 0

# If the count reaches 5, break the loop.
# Else, set value to 0, then continue.
while value3:
    count += 1
    print(count)

    if (count == 5):
        break

    else:
        value3 = 0
        continue
