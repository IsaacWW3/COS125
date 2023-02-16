# File: worcester_hw2a.py
# Author: Isaac Worcester
# Date: 2/2/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Calculates the average lab attendance
# Collaboration:
# Me, Myself and I


print("Hello, I will calculate the class average")
#  this list stores the values for the lab inputs
list = []


# is basically the index for the while loop and is also used at the end to calculate the total lab grades
x = 0
# this while loops allows for the input to be taken 4 times
while x != 4:
    lab = int(input("Enter the attendance for lab: "))
    if lab >= 0 and lab <= 20: # this if statement makes sure they user inputs a valid integer between 0 and 20
        list.append(lab) # this appends the lab variable input into the list
        x += 1 # this adds one to the index, but only if the input falls within the stated perameters
    else: # this else is to print the statement below if wrong input is put in by user
        print("Please enter a valid number below 20 and above -1")


total = 0 # total is to hold the value for the total average
y = 0 # y is the index used for the list to allow for it to calculate properly
for i in list: # this for loop cycles through the index of the ist and adds all the numbers together
    total = list[y] + total
    y += 1

total /= x # this division at calculates the total average of the four labs

print("The attendance average is", round(total))