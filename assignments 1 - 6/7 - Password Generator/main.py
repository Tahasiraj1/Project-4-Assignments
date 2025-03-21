import string
import random


def generate_password(length, amount):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    all_chars = letters + digits + punctuation
    password_list = []

    for _ in range(amount):
        password = ''.join(random.choice(all_chars) for _ in range(length))
        password_list.append(password)

    print("\nHere are your passwords:")
    for pas in password_list:
        print(pas)
        

amount = int(input("\nHow many passwords do you want to generate? "))
length = int(input("\nHow long do you want the passwords to be? "))

generate_password(length, amount)