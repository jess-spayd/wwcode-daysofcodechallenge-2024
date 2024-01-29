# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def even_numbers(num_list: list) -> list:
    
    new_num_list = []

    for num in num_list:

        if num % 2 == 0:
            new_num_list.append(num)

    return new_num_list


random_num_list = [1,2,3,4,5,6,7,8,9]
print(even_numbers(random_num_list))



