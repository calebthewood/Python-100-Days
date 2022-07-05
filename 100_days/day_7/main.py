#Step 5

import random
from re import S
from hangman_art import stages, logo
from hangman_words import word_list
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def play_hangman():
    """Classic game of hangman, 6 guesses"""
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(logo)
    #print(f'Pssst, the solution is {chosen_word}.')
    start = input("enter 'y' to begin or 'n' to exit\n")
    if start == 'n': return

    display = []
    guesses = set()
    for _ in range(word_length):
        display += "_"

    cls()
    print(f"{' '.join(display)}")
    print(stages[lives])

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in guesses:
            print(f"'{guess}' has already been guessed.")
        else:
            cls()
            guesses.add(guess)
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

            if guess not in chosen_word:
                print(f"{guess} is not in the word.")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print(f"You Lose!\nThe word was '{chosen_word}'")

            print(f"{' '.join(display)}")

            if "_" not in display:
                end_of_game = True
                print("You Win!")

            print(stages[lives])

    #play again option
    play_hangman()