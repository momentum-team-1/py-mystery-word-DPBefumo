import random

#function for difficulty level

#function for validating word length for difficulty level

#function to get filtered word from file
def get_filtered_word():
    """
    Opens the file, then puts the words in to strings, to be able to select each word randomly
    """
    opened_file = open('words.txt')
    words = opened_file.read().split()
    print(words[100:110])
#function for random word

#function for displaying the letter

#function for displaying word as it get guessed

#function to get guess 

#function to keep count of guesses

#function for guesses remaining

#function to start game
def start_game(word, guesses):
    pass

if __name__ == "__main__":
    get_filtered_word()