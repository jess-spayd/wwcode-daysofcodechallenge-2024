# Create a program that checks if a year is a leap year.

def leap_year(year: int):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

user_input = int(input("Enter a year: "))

leap_year(user_input)