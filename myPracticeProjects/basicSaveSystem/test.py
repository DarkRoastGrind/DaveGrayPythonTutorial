# r = Read - Prints out file information.
# a = Append - Will create a file if file does not exist.
# w = Write - Overwrites a file.
# x = Create - Creates a file.

import os
import sys

level = "1"
location = "Beginner Island"


def display_save_slots():
    if os.path.exists("myPracticeProjects/basicSaveSystem/save_1.txt"):
        f = open("myPracticeProjects/basicSaveSystem/save_1.txt")
        print(f"\nSlot 1: \n{f.read()}")
    else:
        print(f"\nSlot 1: \nEmpty.")

    if os.path.exists("myPracticeProjects/basicSaveSystem/save_2.txt"):
        f = open("myPracticeProjects/basicSaveSystem/save_2.txt")
        print(f"\nSlot 2: \n{f.read()}")
    else:
        print(f"\nSlot 2: \nEmpty.")

    if os.path.exists("myPracticeProjects/basicSaveSystem/save_3.txt"):
        f = open("myPracticeProjects/basicSaveSystem/save_3.txt")
        print(f"\nSlot 3: \n{f.read()}")
    else:
        print(f"\nSlot 3: \nEmpty.")


def save():
    file_index = 0
    display_save_slots()

    file_index = input(
        f"\nPlease input which save slot you would like to save in, 1, 2, 3, or press 4 to return.\n"
    )

    if file_index not in ["1", "2", "3", "4"]:
        print(f"\nIncorrect input, please chose from the options listed.")
        return save()

    if file_index == "4":
        save_menu_options()

    # If the file exists already,
    if os.path.exists(f"myPracticeProjects/basicSaveSystem/save_{file_index}.txt"):
        confirm = input(
            f"Data exists in slot {file_index}, Do you wish to continue? Y/N"
        )

        if confirm.lower() not in ["y", "n"]:
            print(f"\nIncorrect input.")
            save()

        elif confirm.lower() == "n":
            save()

        else:
            user_name = input(f"\nPlease input a username for the file:\n")
            create_save(user_name, level, location, file_index)
            save_menu_options()

    else:
        user_name = input(f"\nPlease input a username for the file:\n")
        create_save(user_name, level, location, file_index)
        save_menu_options()


def create_save(name, level, location, file_index):
    f = open(
        f"myPracticeProjects/basicSaveSystem/save_{file_index}.txt", "w"
    )

    f.write(f"Name: {name}\nLevel: {level}\nLocation: {location}")
    f.close()
    print("\nFile saved successfully.")


def save_menu_options():
    choice = input(
        "\nPlease select an option:\n1. Save Game\n2. Load Save\n3. Delete Save\n4. Quit\n"
    )

    if choice not in ["1", "2", "3", "4"]:
        print(f"\nIncorrect input, please chose from the options listed.")
        return save_menu_options()

    if choice == "1":
        save_game = save()
        save_game()

    elif choice == "2":
        return

    elif choice == "3":
        return

    elif choice == "4":
        sys.exit()


save_menu_options()


# def save_file_deletion():
#     display_save_slots()
#     # Delete the save file, if it exists.
#     if os.path.exists("myPracticeProjects/basicSaveSystem/save.txt"):
#         os.remove("myPracticeProjects/basicSaveSystem/save.txt")
#     else:
#         print("No save file found, please play the game and create a new save.")

#     # If the save file does not exists, create it.
#     if not os.path.exists("myPracticeProjects/basicSaveSystem/save.txt"):
#         f = open("myPracticeProjects/basicSaveSystem/save.txt", "x")
#         print(f"\nSave file successfully cleared.")
#     f.close()

# def create_save_file(name, level, location):

# # Appending - Creates a file if it doesn't exist
# f = open("Tutorial22/names.txt", "a")
# # Write a new line to the file.
# f.write("\nBitches")
# # Save and close.
# f.close()

# # Open the file for reading.
# f = open("Tutorial22/names.txt")
# print(f.read())
# f.close()
# print()

# # Write (overwrite a file)
# # Open the file for writing.
# f = open("Tutorial22/context.txt", "w")
# # Overwrite all content
# f.write("Big bootie bitches.")
# f.close()

# f = open("Tutorial22/context.txt")
# print(f.read())
# f.close()
# print()

# # Create a new file, two separate ways
# # Opens a file for writing, creates the file if it doesn't exist.
# # Open/Create a file with the given name it doesn't exist.
# f = open("Tutorial22/name_list.txt", "w")
# f.close()

# # Second way to create a new file could cause an error.
# # If the file exists, an error will be returned. try/if

# # If Nicholas.txt does not exist, make it.
# if not os.path.exists("Tutorial22/Nicholas.txt"):
#     f = open("Tutorial22/Nicholas.txt", "x")
#     f.close()

# # Delete file/files
# # Avoid an error if it doesn't exist.

# # If the file exists, delete it, else return message.
# if os.path.exists("Tutorial22/name_list.txt"):
#     os.remove("Tutorial22/name_list.txt")
#     print("File removed.")
# else:
#     print("File does not exist.")


# # Implicit exception handling
# # Open the more_names text file as a baseline,
# with open("Tutorial22/more_names.txt") as f:
#     print("\nmore_names.txt File opened.")
#     content = f.read()

# # And write over the names.txt file, setting it back to default.
# with open("Tutorial22/names.txt", "w") as f:
#     print("\nnames.txt File opened.")
#     f.write(content)
#     print("\nnames.txt: Good overwrite.")
