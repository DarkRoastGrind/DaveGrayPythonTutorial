# r = Read
# a = Append
# w = Write
# x = Create

import os

# Read - Error if it doesn't exist.

# Allocates f to the function of opening the given file.
f = open("Tutorial22/names.txt")

# # Print the contents of the file.
# print(f.read())

# # Read only the first 4 characters of the file.
# print(f.read(4))

# # Read the first line, then  the second line of the file.
# print(f.readline())
# print(f.readline())

# Loop through the entire file, printing all of the lines.
for line in f:
    print(line)

# Close the file following usage. Change will not show until a file is changed.
f.close()
print()

# Error handling for file handling.
try:
    # Check if the file exists,
    f = open("Tutorial22/name_list.txt")
    print(f.read())
except:
    # Return that it doesn't exist if it doesn't,
    print("File does not exist.")
finally:
    # Close the file after all is said and done.
    f.close()
print()

# Appending - Creates a file if it doesn't exist
f = open("Tutorial22/names.txt", "a")
# Write a new line to the file.
f.write("\nBitches")
# Save and close.
f.close()

# Open the file for reading.
f = open("Tutorial22/names.txt")
print(f.read())
f.close()
print()

# Write (overwrite a file)
# Open the file for writing.
f = open("Tutorial22/context.txt", "w")
# Overwrite all content
f.write("Big bootie bitches.")
f.close()

f = open("Tutorial22/context.txt")
print(f.read())
f.close()
print()

# Create a new file, two separate ways
# Opens a file for writing, creates the file if it doesn't exist.
# Open/Create a file with the given name it doesn't exist.
f = open("Tutorial22/name_list.txt", "w")
f.close()

# Second way to create a new file could cause an error.
# If the file exists, an error will be returned. try/if

# If Nicholas.txt does not exist, make it.
if not os.path.exists("Tutorial22/Nicholas.txt"):
    f = open("Tutorial22/Nicholas.txt", "x")
    f.close()

# Delete file/files
# Avoid an error if it doesn't exist.

# If the file exists, delete it, else return message.
if os.path.exists("Tutorial22/name_list.txt"):
    os.remove("Tutorial22/name_list.txt")
    print("File removed.")
else:
    print("File does not exist.")


# Implicit exception handling
# Open the more_names text file as a baseline,
with open("Tutorial22/more_names.txt") as f:
    print("\nmore_names.txt File opened.")
    content = f.read()

# And write over the names.txt file, setting it back to default.
with open("Tutorial22/names.txt", "w") as f:
    print("\nnames.txt File opened.")
    f.write(content)
    print("\nnames.txt: Good overwrite.")
