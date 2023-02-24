# Task 2
# This program will calculate the average grade for each of the students
# and print the average along with their name.

mylist = [
    'John', 55, 89, 102,
    'Sandy', 88, 76, 91,
    'Lisa', 65, 87, 94,
    'Karl', 80, 81, 82,
    'Mabel', 75, 78, 81,
    'Mandy', 56, 92, 87,
    'Evan', 66, 89, 90
]

for i in range(7): # changed range len(mylist) to 7
    total = 0
    for j in range(1,4):
        total += mylist[4*i+j]
    print(f"{mylist[4*i]}'s average is: {total/3}.") # total / 3 instead of 4


