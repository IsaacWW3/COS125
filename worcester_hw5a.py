# File: worcester_hw5a.py
# Author: Isaac Worcester
# Date: 3/9/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description:
# A short program that takes an input for the amount of slogans to generate and outputs randomly generated slogans
# Collaboration:
# Me, Myself and I
import random

name_list = ["Hulk", "Spock", "Ted Lasso", "Aaron Burr", "The Cowardly Lion", "Cinderella",
             "Black Panther", "Merida", "Uhuru", "Freya", "Frodo", "Megan Rapinoe"]
verb_list = ["Leading", "Serving", "Building", "Creating", "Putting", "Fighting", "Taking",
             "Cleaning up", "Protecting", "Putting", "Smashing", "Working", "Coaching", "Kicking"]
direct_objects_list = ["the future", "our community", "jobs", "education", "corruption", "action", "families",
                       "change", "progress", "government", "results", "our enemies"]
adverb_list = ["with integrity", "for you", "first", "safe", "for the future", "for a change", "for Maine",
               "with experience", "with vision"]

def Slogans(n):
    for x in range(0,n):
        print(f"{random.choice(name_list)}: {random.choice(verb_list)} {random.choice(direct_objects_list)} "
              f"{random.choice(adverb_list)}")
Slogans(int(input("How many slogans would you like? ")))