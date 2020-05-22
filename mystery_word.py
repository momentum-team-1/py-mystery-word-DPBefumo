import random

def get_random_word(word):
    """
    Opens the file, then puts the words in to strings, to be able to select each word randomly
    """
    #can add min and max length to it but it will change to filtered word, not random, since the length will dicide the word
    opened_file = open("words.txt")
    lines = opened_file.read()
    word = lines.split()
    opened_file.close()
    return random.choices(word)

#function for setting up difficutly level

#function to display letter
def display_letters(letter, guesses):
    """
    Display a letter if it is in the list of guesses
    """
    if letter in guesses:
        return letter
    else:
        return "_"

#funtion to display word
def display_word(word, guesses):
    """
    Go through the word, for each letter correctly guessed display that letter, else display an underscore
    """
    letters = []
    for letter in word:
        letters.append(display_letters(letter, guesses))

    user_display = " ".join(letters)
    return user_display.upper()
#function for getting next guess

#function for calcualting guesses left

#function for guesses left

#function to run game
    #while loop

# word = []
# get_random_word(word)

if __name__ == "__main__":
    print(display_word("parabola", ["p", "a"]))