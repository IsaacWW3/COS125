# File: worcester_hw4b.py
# Author: Isaac Worcester
# Date: 3/1/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
#
# Collaboration:
# Me, Myself and I

fav_park_list = []
fav_part_list = []
fav_park_attend_list = []
def park_inputs():
    fav_park = 'm'
    while fav_park != 'done': # wasn't triggering when done was entered which is why there is an if break
        fav_park = input("What is one of your favorite Maine parks? (or done to stop): ")
        if fav_park == 'done':
            break
        else:
            fav_park_list.append(fav_park) # appends to list
            fav_part_park = input(f"What is your favorite part of {fav_park}: ") # prints latest item in the list
            fav_part_list.append(fav_part_park)
            fav_park_attend = int(input(f"How many thousand people visit {fav_park} in a year?: ")) # same as anove
            fav_park_attend_list.append(fav_park_attend)
    del fav_park_list[-1]

def park_select(): # didnt get this section working in time
    park_selection = input(f"Which park to celebrate (between 0 and {len(fav_park_list)}): ")
    x = 0
        print(f"At {fav_park_list}, I love,")
        for j in range(fav_park_attend_list[x] / 10):
            print(f"I love {fav_part_list}")
    x += 1



def main():
    park_inputs()
    park_select()

main()