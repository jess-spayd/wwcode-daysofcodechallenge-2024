# Write a program to print the multiplication table of a given number.

def multiplication_table(num: int) -> str:

    for i in range(1,13):
        print(num, 'x', i, '=', num*i)

user_input = int(input('Type an integer: '))

multiplication_table(user_input)

