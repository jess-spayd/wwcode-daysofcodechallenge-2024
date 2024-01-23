# Write a program to shuffle the elements of a list randomly.

import random

list_of_numbers = [1,2,3,4,5,6,7,8,9]

shuffled_list = random.sample(list_of_numbers, len(list_of_numbers))

print(shuffled_list)
