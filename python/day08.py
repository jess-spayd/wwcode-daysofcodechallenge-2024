# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def case_char_count(given_string: str):

    lower_sum = 0
    upper_sum = 0

    for char in given_string:
        if char.islower():
            lower_sum += 1
        elif char.isupper():
            upper_sum += 1
    
    print('Uppercase letters:', upper_sum)
    print('Lowercase letters:', lower_sum)

user_input = input('Type anything: ')
case_char_count(user_input)
