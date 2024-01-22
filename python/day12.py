# Write a program to reverse a given string.

def reverse_string(given_string: str) -> str:
    reverse_string = given_string[::-1]
    return reverse_string

user_input = input('Type anything to reverse it: ')

print(reverse_string(user_input))
