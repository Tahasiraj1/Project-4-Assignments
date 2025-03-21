import click
import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Guessed letters
        print(click.style(f"\nYou've {lives} left, and you've used these letters: {''.join(used_letters)}", fg='yellow'))

        # Current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(click.style(f"\nCurrent word: {''.join(word_list)}\n", fg='green'))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print(click.style(f"\nThe letter is not in word."))

        elif user_letter in used_letters:
            print(click.style("\nYou already guessed that letter.", fg='red'))

        else:
            print('Invalid letter.')

    if lives == 0:
        print(click.style(f"\nGame over, the word was {word}", fg='red'))
    else:
        print(click.style(f"\nYou won! The word was: {word}\n", fg='green'))

hangman()