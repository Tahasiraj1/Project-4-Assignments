import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess > random_number:
            print("Too High!")
        elif guess < random_number:
            print("Too Low!")

    print(f"Congrats you guess the number {x} correctly!!")

guess(5)