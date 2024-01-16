# Write a program to count the occurrences of a specific character in a string.

def count_char(given_string, given_char):

    char_sum = sum(1 for char in given_string if char == given_char)

    print('Count of character:', char_sum)


given_string = input('Type anything: ')
given_char = input('Select a character to count (case sensitive): ')

count_char(given_string, given_char)

