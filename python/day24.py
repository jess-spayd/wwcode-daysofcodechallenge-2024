# Write a program to remove vowels from a given string.

def remove_vowels(given_string: str) -> str:

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_string = given_string

    for character in given_string:

        if character in vowels:
            new_string = new_string.replace(character, "")
    
    return new_string

user_input = input('Type a string: ')

print(remove_vowels(user_input))


