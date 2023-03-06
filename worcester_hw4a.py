# File: worcester_hw4a.py
# Author: Isaac Worcester
# Date: 3/1/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# This program takes 5 inputs for different parks and their attendance and then calculates the maximum and the minimum
# as well as the total and average and the prints back these values to the user
# Collaboration:
# Me, Myself and I

# initialize the lists
park_name = []
park_attend = []

def park_input(): # this function takes the inputs for park name and attendance

    x = 0 # counter for the loop
    while x < 5:
        park_name_input = input("Enter park name: ")
        park_name.append(park_name_input) # this adds the park name to the park_name list
        park_attend_input = int(input("Enter park attendance: "))
        park_attend.append(park_attend_input) # this adds the park attendance to the attendance list
        x += 1

def attendMin():
    minimum = min(park_attend) # uses the min function to get the minimum item in the list
    x = 0
    for i in park_attend: # iterates through the list to find the minimum
        if park_attend[x] == minimum: # if the attendance is equal to the minimum do below
            print(f"The park with the fewest visitors is {park_name[x]} with {minimum} thousand.")
        x += 1

def attendMax():
    maximum = max(park_attend) # uses max function to find maximum number in the list
    j = 0
    for i in park_attend: # does the same thing the minimum function does but for maximum
        if park_attend[j] == maximum:
            print(f"The park with the most visitors is {park_name[j]} with {maximum} thousand.")
        j += 1

def attendTot():
    global total_attend
    total_attend = sum(park_attend) # uses sum function to get the total of the list
    print(f"The total number of visitors at the parks is {total_attend} thousand.")

def attendAvg():
    attend_average = total_attend / len(park_attend) # this caculates the average by using the total and dividing it by the length of the list
    print(f"The average attendance in the parks is {attend_average} thousand.")

def main():
    park_input()
    attendMin()
    attendMax()
    attendTot()
    attendAvg()


main()