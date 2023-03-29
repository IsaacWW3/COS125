# File: worcester_lab5.py
# Author: Isaac Worcester
# Date: 2/26/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# This is the lab 6 excersizes for 3/7/2023
# Collaboration:
# Me, Myself and I
import random


# TASK 0

def diceRoll(num, diceMax):
    total = 0
    for i in range(num):
        x = random.randint(1, diceMax)
        total = total + x
    return total

roll = diceRoll(2, 6)

print(f"The sum of all dice rolls is {roll}")

# -------------------------------------------------------------------------------------------------------------
# TASK 1 A
quote = "Most of the good programmers do programming "+ \
"not because they expect to get "+ \
"paid or get adulation by the public, "+ \
"but because it is fun to program."

def firstWord(sentence):
    return sentence[0:4]

firstWord(quote)
'''
def slicer():
    for i in quote:
        if i != ' ':
            x = i.upper()
            print(x)
        else:
            break
slicer()
'''
# ------------------------------------------------------------------------------------------------------------------
# Task 1 B
