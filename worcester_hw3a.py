# File: worcester_hw3a.py
# Author: Isaac Worcester
# Date: 2/6/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Take an input of numbers and print out the largest number, end loop with 'end'
# Collaboration:
# Me, Myself and I

num = 'm' # this isn't equal to 'end' so it forces the while loop to trigger
list = [] # empty list to store the variables
while num != 'end': # while num doesn't equal the 'end' string
        num = input("Enter a number, or enter 'end' to exit loop: ") # takes the input
        list.append(num) # appends user input to list

list = list[:-1]  # removes last item of the list (in this case it is end)

print("The largest number is,", max(list)) # uses the max function built into python to grab the highest value
