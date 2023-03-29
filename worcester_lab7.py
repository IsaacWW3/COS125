# File: worcester_lab5.py
# Author: Isaac Worcester
# Date: 2/26/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# This is the lab 7 for 3/7/2023
# Collaboration:
# Me, Myself and I
import random


# TASK 1A
def buildRandomList(n, r):
    myList = []
    i = 0
    while i < n:
        randobongo = random.randint(0, r)
        myList.append(randobongo)
        i += 1
    return myList


def main():
    print(buildRandomList(random.randint(1, 9), random.randint(1, 9)))


main()

# ---------------------------------------------------------------------------------------------------------
# TASK 1B
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]

def pruneList(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2


print(pruneList(list1))

# ---------------------------------------------------------------------------------------------------------
# TASK 1C


