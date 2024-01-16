# Write a program to count the occurrences of a specific character in a string.

def count_char(given_string, given_char):

    given_string_lower = given_string.lower()
    given_char_lower = given_char.lower()

    char_sum = sum(1 for char in given_string_lower if char == given_char_lower)

    print('Count of character:', char_sum)


given_string = input('Type anything:')
given_char = input('Select a character to count:')

count_char(given_string, given_char)

