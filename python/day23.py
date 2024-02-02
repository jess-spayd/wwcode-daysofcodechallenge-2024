# Write a program that checks if a key exists in a dictionary.

my_dict = {

    'Jabba': 4,
    'Sweetie': 8,
    'Liddle': 3,
    'Sammy': 10,
    'Jack': 5,
    'Marty': 11,
    'Max': 1

}

def check_keys(my_dict: dict, given_key: str) -> bool:

    if given_key in my_dict:
        return True
    else:
        return False

user_input = input("Enter a name to check if it exists in my dictionary: ")

print(check_keys(my_dict, user_input))
