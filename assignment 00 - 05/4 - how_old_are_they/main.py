def main():
    persons = [
    {"name": "Anton", "age": 21},
    {'name': 'Beth', 'age': 27},
    {'name': 'Chen', 'age': 47},
    {'name': 'Drew', 'age': 68},
    {'name': 'Ethan', 'age': 47},
    ]

    for person in persons:
        print(f'{person['name']} is {person['age']}\n')



if __name__ == '__main__':
    main()