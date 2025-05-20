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

# Nested Dictionaries 
member1 = {
    "name": "Plant",
    "Instrument": "vocals"
}

member2 = {
    "name": "Plant",
    "Instrument": "vocals"
}

