# File: worcester_hw1b.py
# Author: Isaac Worcester
# Date: 1/24/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Asks a user for price of icecream, calculates 3 bars cost, calculates sale tax, adds them together to get total cost
# spits out total cost to user
# Collaboration:
# Me, Myself and I

price = int(input("How much is this icecream bar?: "))

three_bar = price * 3
tax_bar = three_bar * 0.055
total_cost = three_bar + tax_bar

print("I would like three bars. Here is $", total_cost)
print("Thank you")