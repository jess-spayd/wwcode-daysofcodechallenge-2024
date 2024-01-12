# Write a function to count the number of vowels in a given string.

def count_vowels(given_string):

    # Convert given string to lowercase
    given_string_lower = given_string.lower()

    # Define vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize sum of vowels
    vowel_sum = 0

    # Iterate over string
    for character in given_string_lower:
        if character in vowels:
            # Add 1 to the sum of vowels
            vowel_sum += 1

    # Print result
    print('Total vowels (excluding Y):', vowel_sum)


# Prompt user to enter a string
given_string = input('Type anything:')

# Run function
count_vowels(given_string)