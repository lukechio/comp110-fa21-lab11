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

    for line in card_file:
        # Replace the following line with lines that split the line and add it to a dictionary
        # Use the `strip` function to ensure that the answer doesn't include a
        # newline character (i.e. '\n')
        fields = line.strip().split("|")
        eng = fields[0]
        esp = fields[1]
        d[eng] = esp
    return d


def quiz(cards, target_score):
    """
    Creates the quiz for the user with the desired flashcards 

    Parameters: cards and target score

    Returns: Total number of questions it tok for the user to reach their target score
    """

    questions = list(cards.keys())
    score = 0
    num_tries = 0
    while score < target_score:
        num_tries += 1
        q = random.choice(questions)
        a = cards[q]
        print(q)
        response = input('Answer: ')
        if response == a:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    return num_tries


# To Do: Define your quiz function immediately AFTER this line.

def main():
    """Prints out the input for the user, and ask the user a series of questions

    Parameters: none

    Returns : what percentage they got on the quiz
    """

    print("Welcome to Flash dance, an amazing Flash Card app")
    fc_filename = input("Enter the name of the flash card file: ")
    cards = get_flash_cards(fc_filename)
    target = int(input("Enter your target score"))
    tries = quiz(cards, target)
    rate = (target/tries) * 100
    print("You got the following percent right: ", rate)


""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
