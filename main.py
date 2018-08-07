import random

words = ["banana", "apple", "orange", "strawberry", "mango"]
max_guesses = 5


# Main menu for user choices
def menu():
    return int(input(
        "Welcome to Hangman! Please select an option:\n" +
        "1. Start Game \n" +
        "2. Quit \n"))


# Receives word input and outputs 'blank' word in Hangman style ex. "_ _ _ _"
def word_blanks(word):
    blanks = []
    for letter in word:
        blanks.append(" _ ")
    return blanks


def hangman():
    print("Welcome to Hangman!\n")

    user_guesses = 0
    challenge_word = random.choice(words)
    blank_word = word_blanks(challenge_word)
    guessed_letters = []

    while user_guesses <= max_guesses:
        # Receives guessed letter and adds it to list
        print("Your word: ", "".join(blank_word),
              "\n Guess ", user_guesses, " of ", max_guesses)
        print("Guessed letters: ", "".join(guessed_letters))

        guess_letter = input("Guess a letter:\n")
        guessed_letters.append(guess_letter)

        # If match is found, updates position in blanks list to letter
        # TODO: Fix loop below. Unable to iterate through word and update
        # TODO: guess letter to blank word if correct
        for i in range(len(challenge_word)):
            if challenge_word[i] == guess_letter:
                blank_word[i] == guess_letter
        user_guesses = user_guesses + 1


user_input = menu()

if user_input == 2:
    print("Goodbye!")
else:
    hangman()
