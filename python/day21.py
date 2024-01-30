# Create a program to remove a specific element from a set.

grocery_list = {'tomato', 'bread', 'tofu', 'cream cheese', 'pickles', 'garlic', 'oats', 'mango'}

print("Grocery list:")
for item in grocery_list:
    print(item)

crossed_item = input("Which item can I cross off the list? ")

if crossed_item in grocery_list:
    grocery_list.remove(crossed_item)
    print("Grocery list:")
    for item in grocery_list:
        print(item)
else:
    print(crossed_item + " isn't on the grocery list.")
