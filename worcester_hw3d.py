# File: worcester_hw3d.py
# Author: Isaac Worcester
# Date: 2/6/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Takes two inputs for first and second number and prints the multiples
# Collaboration:
# Me, Myself and I

def main(x, y):
    num = (range(1, y + 1))
    multiply12 = range(1, x + 1)
    for a in multiply12:
        for b in num:
            print(f"{a * b}", end=" ")
        print()


main(int(input("Please enter your first number: ")), int(input("Please enter your second number: ")))()
