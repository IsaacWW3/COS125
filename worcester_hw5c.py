# File: worcester_hw5a.py
# Author: Isaac Worcester
# Date: 3/9/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Collaboration:
#
import random


def main():

    score = 0  # initialize score variable

    while score < 20:
        roll = random.randint(1, 6)  # Selects a random number between 1 and six
        score += roll  # adds randomly generated roll value to the score
        print(f"Roll: {roll}")  # prints roll value

        if roll == 1:  # checks if roll value is 1
            print("Turn Total: 0")  # print is 0
            score=21  # sets score to 21 to end the loop
        else:
            print(f"Turn Total: {score}")  # if it is not one, it will print the score until it is 20 or above
main()