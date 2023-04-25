# File: worcester_project1.py
# Author: Isaac Worcester
# Date: 4/4/2023
# Section: 3:30pm on Tuesdays
# E-mail: isaac.worcester@maine.edu
# Description: This program opens and reads the movie review file and assigns a score to each word, it also can take
# a user input for a file or word and calculate the score based off of the original movie review file
# Collaboration:
# No one
def calc_sentiment(user_word):  # calculates the sentiment for single words
    with open("movieReviews.txt", "r") as file:  # open the file
        # initialize variables
        counter = 0
        total_score = 0
        for line in file:
            #  Split the line into words
            words = line.split()
            if user_word in words:
                score = int(line[0])  # since the score is always at the first index, check first index
                total_score += score
                counter += 1
    if counter > 0:
        average_score = total_score / counter  # calculates the average score for a word in the file
    else:
        average_score = 0  # the average score for a word not in the file is 0

    return average_score

def user_file_score(filename): # gives a score for the user entered file
    # initialize the total score and counter at the top
    total_score = 0
    counter = 0


    with open(filename, 'r') as file:  # open the user entered file

        for line in file:  # this loops through each line in the file
            words = line.split()   # uses the split function to separate the words in the lines
            for word in words:
                score = calc_sentiment(word)  # checks the score for every word
                total_score += score  # adds the score to the total score
                counter += 1  # increment the counter
    if counter > 0:  # if the counter is higher than 0 it will get the average score
        average_score = total_score / counter
    else: # if the word doesn't exist in words it will just be 0
        average_score = 0
    return average_score

def highest_lowest(filename): # calculates the highest and lowest word in the user given file
    # declaring variables, highest and lowest word are blank strings since they will be replaced
    # highest score is -1 since no value will be lower than that, lowest score is 100000 since no score will be higher
    highest_word = ""
    highest_score = -1
    lowest_word = ""
    lowest_score = 100000

    with open(filename, 'r') as file:  # opens the file
        for line in file:  # this loops through each line in the file
            words = line.split()  # uses the split function to separate the words in the lines
            for word in words:
                score = calc_sentiment(word)  # this calls the first function and searches it for each word, setting it
                # equal to score so that it can run the below checks for highest and lowest number
                if score > highest_score:  # checks to see if score of the word is more than highest score
                    highest_word = word  # if true, highest word will be set to word
                    highest_score = score  # if true, highest score will be set to score
                if score < lowest_score:  # this is exactly the same as highest but for lowest
                    lowest_word = word
                    lowest_score = score
    # this function returns all these values so they can be used and printed in main
    return highest_word, highest_score, lowest_word, lowest_score

def main():
    # print out all the options for the menu
    print("What would you like to do?\n"
          "1. Calculate the highest sentiment score of a single word?\n"
          "2. Calculate the average score of words in a file\n"
          "3. Find the highest and lowest scoring words in a file\n"
          "4. Exit the program")

    user_input = int(input("Enter a number 1-4: "))  # take the user input for the menu
    while user_input != 4:  # terminate the program if 4 is entered

        if user_input == 1:  # Calculate the highest sentiment score of a single word
            user_word_select = input("Enter a word: ")
            score = calc_sentiment(user_word_select)  # function call for the sentiment of the word
            print(f"The average sentiment score for reviews containing the word '{user_word_select}' is {score:.2f}")
            break

        elif user_input == 2:  # Calculate the average score of words in a file
            user_file_name2 = input("Enter file name: ")
            score1 = user_file_score(user_file_name2)
            print(f"The average score of the words in {user_file_name2} is {score1:.2f}")
            break


        elif user_input == 3:  # Find the highest and lowest scoring words ina  file
            user_file_name3 = input("Enter file name: ")
            # the reason this has 4 variables assigned to it is because they all correspond to the 4 return values of
            # the function
            high_word, high_score, low_word, low_score = highest_lowest(user_file_name3)

            print(f"The highest word is {high_word}, with a score of {high_score}")  # prints the highest value and score
            print(f"The lowest word is {low_word}, with a score of {low_score}")  # prints the lowest value and score
            break

        else:  # Check for valid input
            print("Enter valid input")
            user_input = int(input("Enter a number 1-4: "))

    print("Program terminated")  # final print statement to let user know the program was terminated

main()