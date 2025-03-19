import random

def main():
    target = random.randint(1, 99)

    print("\nIm thinking of a number between 1 and 99.\n")
    
    while True:
        guess = int(input("Enter a new number: ")) 

        if guess == target:
            print(f"Congrats! The number was: {target}")
            break
        elif guess < target:
            print("Your guess is too low")
        elif guess > target:
            print("Your guess is too high")



if __name__ == '__main__':
    main()