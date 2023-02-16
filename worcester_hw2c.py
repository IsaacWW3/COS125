# File: worcester_hw2c.py
# Author: Isaac Worcester
# Date: 2/2/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# A recycling coat bot that tells you how may bottles you used vs recycled
# Collaboration:
# Me, Myself and I

bottle_use = int(input("How many bottles did you use today?: "))
bottle_gone = int(input("How many bottles did you recycle today?: "))

if bottle_gone == bottle_use:
    print("Congratulations, you recycled as many bottles as you used!",
          "Have you thought about using a reusable bottle? It's better for the environment!",
          "Remember to visit Boardman 138 for help or community.", sep='\n')
elif bottle_gone > bottle_use:
    print("How did you manage to recycle more than you used? Your integrity is unmatched!",
          "Have you thought about using a reusable bottle? It's better for the environment!",
          "Remember to visit Boardman 138 for help or community.", sep='\n')
else:
    print("You only recycled,", bottle_gone, "bottles today but used,", bottle_use, ",meaning you have",
          bottle_use - bottle_gone, "left to recycle, do better tomorrow.")
    print("Have you thought about using a reusable bottle? It's better for the environment!",
          "Remember to visit Boardman 138 for help or community.", sep='\n')
