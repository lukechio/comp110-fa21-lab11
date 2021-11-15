"""
Module: comp110_lab11

Lab 11: A flash card program.
"""
import random


def get_flash_cards(filename):
    """
    Creates a dictionary of flash card questions and answers.

    Parameters:
    filename (type: string) - The name of the file containing flash card Q's/A's

    Returns:
    (type: dictionary) - A dictionary that associates questions with answers.
    """

    card_file = open(filename, 'r')
    d = {}

    my_dict = {}

    for line in card_file:
        new_line = line.strip

        # Replace the following line with lines that split the line and add it to a dictionary
        # Use the `strip` function to ensure that the answer doesn't include a
        # newline character (i.e. '\n')
        pass


def quiz(cards, target_score):
    """
    Creates the quiz for the user with the desired flashcards 

    Parameters: cards and target score

    Returns: Total number of questions it tok for the user to reach their target score
    """

    return None  # modify this line to return your dictionary


# To Do: Define your quiz function immediately AFTER this line.

def main():
    """Prints out the input for the user, and ask the user a series of questions

    Parameters: none

    Returns : what percentage they got on the quiz
    """

    print("Welcome to Flash in the pan, a Flash Card Program")

    input("Enter the name of the file would like to see flashcards for")

    input("Enter the score you would like to target on this quiz")

    print()


""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
