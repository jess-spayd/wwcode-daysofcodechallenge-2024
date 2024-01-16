# Write a program to check if a number is positive, negative, or zero.

def number_check(given_number: float):

    if given_number > 0:
        print('This number is positive.')
    elif given_number < 0:
        print('This number is negative.')
    else:
        print('This number is zero.')

given_number = float(input('Enter a number: '))

number_check(given_number)
