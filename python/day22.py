# Create a program to find the second-largest element in a list.

num_list = [1,2,3,4,5,6,7,8,9]

# Find the largest number in the list
max_num = max(num_list)

# Make a copy of the list
num_list_new = num_list[:]

# Remove the largest number from the copied list
num_list_new.remove(max_num)

# Find the largest number in the new list
max_second_num = max(num_list_new)

print(num_list)
print("The second largest number is " + str(max_second_num))

