import random

#function for difficulty level

#function for validating word length for difficulty level

#function to get filtered word from file - needs min and max length added when difficulty is set up
def get_filtered_word():
    """
    Opens the file, then puts the words in to strings, to be able to select each word randomly
    """
    opened_file = open('words.txt')
    words = opened_file.read().split()
    opened_file.close()
    filtered_word = [word for word in words]
    
    return filtered_word
    
#function for random word - needs min and max length added when difficulty is set up
def get_random_word():
    """
    Take the filtered words and pick out a random one for the player to guess
    """
    return random.choice(get_filtered_word())

#function for displaying the letter - complete
def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"

#function for displaying word as it get guessed - complete
def display_word(word, guesses):
    """
    Go through the word, for each letter correctly guessed display that letter, else display an underscore
    """
    output_letters = [display_letter(letter, guesses) for letter in word]

    user_display = " ".join(output_letters)

    return user_display.upper()

#function to get guess - complete
def get_next_guess():
    """
    Ask the user to guess a letter, and then return that letter lowercase
    """
    user_guess = input('Guess a letter: ')
        
    return user_guess.lower()

#function to keep count of guesses
def calc_guesses_remain(word, guesses):
    """
    Calculate the remaining number of guesses by comparing guess not being in word, then subtracting it from the 8 overall guesses
    """
    wrong_guess = []
    for guess in guesses: 
        if guess not in word:
            return 8 - len(wrong_guess)

#function for guesses remaining
def guesses_remain(word, guesses):
    """
    Will take the calculated guesses left so that it can validate if the number of remaining guesses are > 0
    """
    guesses_remain = calc_guesses_remain(word, guesses)
    return guesses_remain > 0

#function to start game
def start_game():
    """
    Combines all functions to run the game.  Produces the random word and takes the guess to see if it is in the word, only takes guesses while there are guesses remaining
    """
    word = get_random_word()
    guesses = []

    while guesses_remain(word, guesses):
        print(display_word(word, guesses))
        guesses.append(get_next_guess())

#function to play again

if __name__ == "__main__":
    start_game()