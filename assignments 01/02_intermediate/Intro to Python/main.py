planets = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14,
}

earth_weight = float(input("\nEnter a weight on Earth: "))

planet = input("Enter a planet: ").strip().capitalize()

if planet in planets:
    equivalent_weight = round(earth_weight * planets[planet], 2)
    print(f"The equivalent weight on {planet}: {equivalent_weight:.2f}")
else:
    print("Invalid planet name. Please try again.")