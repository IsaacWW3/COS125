# File: worcester_hw3b.py
# Author: Isaac Worcester
# Date: 2/6/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# Take an input of numbers and calculates leap year
# Collaboration:
# Me, Myself and I

loop = True # set loop to true for while loop to run
while loop is True: # this means literally what it says, while loop is true, do below
    f_year = int(input("Enter first year: ")) # input for first year
    l_year = int(input("Enter last year: ")) # input for last year
    if l_year <= f_year: # if last year is less than first year, print enter valid input and run loop again
        print("Please enter valid input")
    else: # else, (which means correct input was done)
        for i in range(f_year, l_year): # this basically says for index in range of whatever two numbers are input
            print(f_year)
            leap = f_year % 4 # mod 4 to figure out which years are leap years, stored in leap variable
            if leap == 0: # checks if what was modded is 0
                print("Is a leap year")
            f_year += 1 # adds one to f_year and will repeat until the number is equal to l_year
        loop = False # once the for loop is completed it will set loop to false, which will end the while loop

# this was originally how I did the program until i re-read the instructions and saw that we had to use range()
'''
       while f_year != l_year:
           print(f_year)
           leap = f_year % 4
           if leap == 0:
               print("Is a leap year")
           f_year += 1
       loop = False
   '''