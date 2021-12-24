# Murtajiz Mehdi
# July 18, 2021
# Create a program that completes given Snack Bar Menu

# Define main function
def main():
    # Declare and initialize all variables
    menuChoice = '0'

    # Declare and initialize all constants
    personalPizza = 6.00
    pretzel = 2.50
    chips = 1.25
    hotDog = 3.75
    tax = 0.07

    # Display Introduction
    print(30 * '-')
    print('Welcome to the snack bar menu!')
    print(30 * '-')
    print('\n\n\n')
    print('Please choose from the options below:')

    # Repeat the following code until user chooses 1, 2, 3, 4, or 5
    while menuChoice != '1' and menuChoice != '2' and menuChoice != '3' and menuChoice != '4' and menuChoice != '5':

        # Display menu bar
        print(f'1) Personal Pizza ${personalPizza:.2f}')
        print(f'2) Pretzel ${pretzel:.2f}')
        print(f'3) Chips ${chips:.2f}')
        print(f'4) Hot Dog ${hotDog:.2f}')
        print('5) Exit\n\n')

        # Prompt user for menu choice
        menuChoice = input('Enter your choice here: ')

        # Enter 'try' function here and indent rest of code from here

        # Create decision structure
        if menuChoice == '1':
            print(f'Your total is ${personalPizza * tax + personalPizza:.2f}')
        elif menuChoice == '2':
            print(f'Your total is ${pretzel * tax + pretzel:.2f}')
        elif menuChoice == '3':
            print(f' Your total is ${chips * tax + chips:.2f}')
        elif menuChoice == '4':
            print(f'Your total is ${hotDog * tax + hotDog:.2f}')
        elif menuChoice == '5':
            print('Have a wonderful day!')
        else:
            print('Please choose between 1-5')

    # Display outro
    print('Thank you for using our menu!')

main()