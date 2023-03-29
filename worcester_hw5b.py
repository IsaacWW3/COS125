# File: worcester_hw5a.py
# Author: Isaac Worcester
# Date: 3/9/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Takes a user input for the name and makes a song from it Has special cases for vowels and names that start with the
# letters B, M, or F
# Collaboration:
# Greg Michaud

def namesong():
    name = ""  # initialize name variable
    while name != "quit":
        # Takes input for the name
        name = input("Name to use: ")
        # If user types "quit", print gooodbye message
        if name == "quit":
            print("OK. Goodbye!")
        # Special Case 1
        elif (name[0:1]) == "A" or (name[0:1]) == "E" or (name[0:1]) == "I" or (name[0:1]) == "O" or (name[0:1]) == "U":
            if name[0:1] == "A":
                print(f"{name}, {name}, bo-ba{name[1:len(name)]}")
                print(f"Banana-fana fo-fa{name[1:len(name)]}")
                print(f"Fee-fi-mo-ma{name[1:len(name)]}")
                print(f"{name}!")
            elif name[0:1] == "E":
                print(f"{name}, {name}, bo-be{name[1:len(name)]}")
                print(f"Banana-fana fo-fe{name[1:len(name)]}")
                print(f"Fee-fi-mo-me{name[1:len(name)]}")
                print(f"{name}!")
            elif name[0:1] == "I":
                print(f"{name}, {name}, bo-bi{name[1:len(name)]}")
                print(f"Banana-fana fo-fi{name[1:len(name)]}")
                print(f"Fee-fi-mo-mi{name[1:len(name)]}")
                print(f"{name}!")
            elif name[0:1] == "O":
                print(f"{name}, {name}, bo-bo{name[1:len(name)]}")
                print(f"Banana-fana fo-fo{name[1:len(name)]}")
                print(f"Fee-fi-mo-mo{name[1:len(name)]}")
                print(f"{name}!")
            elif name[0:1] == "U":
                print(f"{name}, {name}, bo-bu{name[1:len(name)]}")
                print(f"Banana-fana fo-fu{name[1:len(name)]}")
                print(f"Fee-fi-mo-mu{name[1:len(name)]}")
                print(f"{name}!")
        # Special Case 2
        elif (name[0:1]) == "B" or (name[0:1]) == "F" or (name[0:1]) == "M":

            if name[0:1] == "B":
                print(f"{name}, {name}, bo-{name[1:len(name)]}")
                print(f"Banana-fana fo-f{name[1:len(name)]}")
                print(f"Fee-fi-mo-m{name[1:len(name)]}")
                print(f"{name}!")
            elif name[0:1] == "F":
                print(f"{name}, {name}, bo-b{name[1:len(name)]}")
                print(f"Banana-fana fo-{name[1:len(name)]}")
                print(f"Fee-fi-mo-m{name[1:len(name)]}")
                print(f"{name}!")
            elif name[0:1] == "M":
                print(f"{name}, {name}, bo-b{name[1:len(name)]}")
                print(f"Banana-fana fo-f{name[1:len(name)]}")
                print(f"Fee-fi-mo-{name[1:len(name)]}")
                print(f"{name}!")
        else:
            print(f"{name}, {name}, bo-b{name[1:len(name)]}")
            print(f"Banana-fana fo-f{name[1:len(name)]}")
            print(f"Fee-fi-mo-m{name[1:len(name)]}")
            print(f"{name}!")


namesong()