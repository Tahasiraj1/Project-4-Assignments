def main():
    user_input = int(input("Enter a number to double: "))
    curr_value = user_input

    while curr_value < 100:
        prev_val = curr_value
        curr_value *= 2
        print(f"{prev_val} doubled is {curr_value}")


if __name__ == '__main__':
    main()