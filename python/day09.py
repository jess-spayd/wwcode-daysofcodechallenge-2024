# Write a program to check if a number is even or odd.

def even_odd(given_int: int):

    if given_int % 2 == 0:
        return 'This number is even.'
    else:
        return 'This number is odd.'

user_input = int(input('Enter an integer: '))

print(even_odd(user_input))