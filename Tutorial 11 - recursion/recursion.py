# Recursive function
def add_one(num):
    # If the num is >= 9, return
    if(num>=9):
        return num + 1
    
    # Total = num+1
    total = num + 1
    print(total)
    
    # Call self to continue adding to total. 
    return add_one(total)

# Recursively increments the input number. 
add_one(0)
print()

# Recursive function
def add_one(num):
    # If the num is >= 9, return
    if(num >= 9):
        return num + 1
    
    # Total = num+1
    total = num + 1
    print(total)
    
    # Call self to continue adding to total. 
    return add_one(total)

# mynewtotal will increment until it's final value of 10. 
mynewtotal = add_one(0)
print(mynewtotal)





