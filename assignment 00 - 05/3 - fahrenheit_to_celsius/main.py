def main():
    degrees_fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    degree_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {degrees_fahrenheit:.1f}F = {degree_celsius}C")


if __name__ == '__main__':
    main()