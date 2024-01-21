# Write a program to remove duplicates from a list.

names = ['Bob', 'Mary', 'Carol', 'Joe', 'Joe', 'Mary', 'Bob', 'Carol']
names_new = []

for i in names:
    if i not in names_new:
        names_new.append(i)

print(names_new)
