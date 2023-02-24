# File: worcester_hw3c.py
# Author: Isaac Worcester
# Date: 2/6/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Reads the list and prints the list in order, then prints the middle list value as the favorite
# Collaboration:
# Me, Myself and I


anime = ['slime', 'chainsaw man', 'demon slayer', 'love is war', 'rent-a-girlfriend', 'domestic girlfriend']

print("The anime list is: ")
x = 0
for i in anime:
    print(x, ":", i)
    x +=1

long_anime = len(anime)

half_anime = long_anime * 0.5

print("My favorite anime is ", anime[int(half_anime)])