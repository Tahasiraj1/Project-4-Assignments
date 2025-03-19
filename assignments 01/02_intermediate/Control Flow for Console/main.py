import random
import click


welcome = "\nWelcome to the High-Low Game!"
print(welcome)
dashes = len(welcome) * "-"
print(dashes)
score = 0
orbit = 0

while True:
    orbit += 1

    if score == 5:
        message = click.style("Wow! You played perfectly!", fg='green')
    elif score > 5 // 2:
        message = click.style("Good job, you played really well!", fg='yellow')
    else:
        message = click.style("Better luck next time!", fg='red')

    if orbit == 6:
        print('-' * len(message))
        print(message)
        print('-' * len(message))
        print("Thanks for playing!")
        break

    computer_num = random.randint(1, 100)
    player_num = random.randint(1, 100)

    print(f"Round {orbit}")
    print(f"Your number is {player_num}")
    
    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

    if player_num > computer_num and guess == 'higher':
        print(click.style(f"\nYou were right! The computer's number was {computer_num}", fg='green'))
        score += 1
        print(click.style(f"Your score is now {score}\n", fg='green'))
    elif player_num < computer_num and guess == 'lower':
        print(click.style(f"\nYou were right! The computer's number was {computer_num}", fg='green'))
        score += 1
        print(click.style(f"Your score is now {score}\n", fg='green'))
    else:
        print(click.style(f"\nAww, that's incorrect. The computer's number was {computer_num}", fg='red'))
        print(click.style(f"Your score is now {score}\n", fg='red'))