# Write a function to calculate the factorial of a number.

def factorial_calculator(num: int) -> int:

    num1 = 1
    result = 1

    while num1 <= num:
        result = num1 * result
        num1 += 1

    return result

given_num = int(input("Enter an integer to calculate its factorial: "))
print(factorial_calculator(given_num))
