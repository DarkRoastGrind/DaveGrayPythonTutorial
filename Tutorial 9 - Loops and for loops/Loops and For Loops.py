print()
# Dictionaries - Used to store data values that are in key value pairs. 
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# Constructor for dictionary
band2 = dict(vocals = "Plant", guitar = "Page")

# Both print out the same structures.
print(band)
print(band2)
print()

# Check the type and length of the dictionary. 
print(type(band))
print(len(band))
print()

# Access items in a dictionary
print(band["vocals"])
print(band.get("guitar"))
print()

# List all keys in the dictionary. 
print(band.keys())
print()

# List all values.
print(band.values())
print()

# List of key/value pairs as tuples
print(band.items())
print()

# Verify a key exists
print("guitar" in band)
print("triangle" in band)
print()

# Change values in a dictionary. 
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)
print()

# Remove items - Returns last item. 
print(band.pop("bass"))
print(band)
print()

# Adds drums, bonham for the next removal using popitem.
band["drums"] = "Bonham"
print(band)
print()

# Removes last key/value pair added to the dictionary. Returns tuple. 
print(band.popitem())
print(band)
print()

# Delete/clear items
band["drums"] = "Bonham"
del band["drums"]
print(band)
print()

# Clearing band 2 entirely. 
band2.clear()
print(band2)
print()

# Completely delete band 2
del band2
print()

# Copy dictionaries

# Doesn't create copy, only reference. 
# band2 = band
# print("Bad copy!")

# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

# Example of a good copy. 
band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)
print()

# Use of constructor for copying dictionaries. 
band3 = dict(band)
print("Good copy!")
print(band3)
print()

# Nested Dictionaries 
member1 = {
    "name": "Plant",
    "Instrument": "vocals"
}

member2 = {
    "name": "Page",
    "Instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

# Print the band that contains the nested dictionaries of member1 and member 2
print(band)

# Print specific elements of the nested dictionaries. 
print(band["member1"]["name"])
print()

# Sets
# Example of a set
nums = {1,2,3,4}
# Constructor function
nums2 = set((1,2,3,4))

print()
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed in sets. will only show one two from below. 
nums3 = {1, 2, 2, 3}
print(nums3)
print()

# True value is a dupe of 1, false is a dupe of 0

# This will print False, 1, 2, 3, 4. 
# True will be ignored, and 0 will be ignored. 
# False comes first, the set is always ordered. 
nums4 = {1, True, 2, False, 5, 3, 4, 0}
print(nums4)
print()

# Check if value in set
print(2 in nums4)
print()

# Cannot refer to an element in a set with an index position, or a key. 

# Adding element to sets. 
nums4.add(8)
print(nums4)
print()

# Remove elements from sets. 
nums4.remove(8)
print(nums4)
print()

# Add elements from another set to another set. 
morenums = {5, 6, 7}
nums4.update(morenums)
print(nums4)
print()

# Can use update with lists, tuples, and dictionaries.


# merge 2 sets to create a new set. 
setone = {1, 2, 3}
settwo = {5, 6, 7}
newset = setone.union(settwo)
print(newset)
print()

# Keep only duplicates of two separate sets. This changes the first set to only include
# duplicates from both sets. 
setone = {1, 2, 3, 5, 7, 9, 11, 12}
settwo = {2, 5, 11, 12}
setone.intersection_update(settwo)
print(setone)
print()

# Keep everything except duplicates. Modifies original input. 
setone = {1, 2, 3, 5, 7, 9, 11, 12}
settwo = {2, 5, 11, 12}
setone.symmetric_difference_update(settwo)
print(setone)
print()

