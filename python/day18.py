# Create a program to find the largest among three numbers.

num_list = []
first_num = input("What's the first number? ")
num_list.append(int(first_num))
second_num = input("What's the second number? ")
num_list.append(int(second_num))
third_num = input("What's the third number? ")
num_list.append(int(third_num))
print("The largest number is " + str(max(num_list)))