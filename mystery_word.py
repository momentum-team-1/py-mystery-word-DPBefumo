import random

#function for setting up difficutly level
def get_difficulty():
    pass

#function to validate word length for different difficulty levels
def validate_word():
    pass

#function to get filtered word from word.txt
#add min and max length, the length will decide the word by difficulty 
def get_filtered_word():
    """
    Opens the file, then puts the words in to strings, to be able to select each word randomly
    """
    opened_file = open("words.txt")
    words = opened_file.read().split()
    opened_file.close()
    filtered_words = [word for word in words]

    return filtered_words

#funtion to get random word
#add min and max length, the length will decide the word by difficulty 
def get_random_word():
    return random.choice(get_filtered_word())

#function to display letter
def display_letter(letter, guesses):
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
    letters = [display_letter(letter, guesses) for letter in word]

    user_display = " ".join(letters)

    return user_display.upper()

#function for getting next guess
def get_next_guess():
    """
    Ask the user to guess a letter, and then return that letter uppercase (may need to be lowercase, *check for error*)
    """
    guessed_letter = input("Guess a letter: ")
    return guessed_letter.upper()

#function for calcualting guesses left
#for loop
def calc_guesses_remain(word, guesses):
    """
    calculate the remaining number of guesses by comparing guess not being in word, then subtracting it from the 8 overall guesses
    """
    pass

#function for guesses left
def guesses_remain(word, guesses):
    """
    Will take the calculated guesses left so that it can validate if the number of remaining guesses are > 0
    """
    pass

#function to run game
    #while loop
def run_game():
    """
    Combines all functions to run the game.  Produces the random word and takes the guess to see if it is in the word, only takes guesses while there are guesses remaining
    """
    word = get_random_word()
    guesses = get_next_guess()
    print(display_word(word, guesses))

#runs the game
if __name__ == "__main__":
    run_game()