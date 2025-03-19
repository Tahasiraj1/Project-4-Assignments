import click

# Accessing Elements
def accessing_el(array, index):
    try: 
        return array[index]
    except IndexError:
        return click.style("Index out of range.", fg='red')


# Modifying Elements
def modify_list(array, index, new_val):
    try:
        array[index] = new_val
        return array
    except IndexError:
        return click.style("Index out of range.", fg='red')


# Slicing the List
def slice_list(array, start_i, end_i):
    try:
        return array[start_i:end_i]
    except:
        return click.style("Invalid indices", fg='red')



def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(click.style(f"\nCurrent list: {fruit_list}", fg='green'))
    choice = input(click.style("\nChoose an option: access, modify, or slice: ", fg='yellow')).strip().lower()

    if choice == 'access':
        index = int(input("Enter an index to access: "))
        print(click.style(accessing_el(fruit_list, index), fg='green'))

    elif choice == 'modify':
        index = int(input("Enter an index to modify: "))
        element = input("Enter an element to modify with: ")
        print(click.style(modify_list(fruit_list, index, element), fg='green'))

    elif choice == 'slice':
        start = int(input("Enter an index to start slicing: "))
        stop = int(input("Enter an index to stop slicing at: "))
        print(click.style(slice_list(fruit_list, start, stop), fg='green'))      

    

if __name__ == '__main__':
    main()