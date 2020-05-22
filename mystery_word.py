import random

#function for setting up difficutly level
def get_difficulty():
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
    pass

#function for calcualting guesses left
def calc_guesses_left():
    pass

#function for guesses left
def guesses_left():
    pass

#function to run game
    #while loop
def run_game():
    """
    Combines all functions to run the game.  Produces the random word and takes the guess to see if it is in the word
    """
    word = get_random_word()
    print(word)
    


if __name__ == "__main__":
    run_game()
    