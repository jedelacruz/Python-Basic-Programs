"""
8. List Concatenation:
Write a program that takes two lists as input and creates a new list by concatenating them.
"""

list1 = []
list2 = []

while True:
    list1Ask = input("Enter list1 items (q to quit): ")
    if list1Ask.lower() == "q":
        break
    else:
        list1.append(list1Ask)

while True:
    list2Ask = input("Enter list2 items (q to quit): ")
    if list2Ask.lower() == "q":
        break
    else:
        list2.append(list2Ask)

combinedList = list1 + list2

print()

print("The list1 is:")
print(list1)

print()

print("The list2 is:")
print(list2)

print()

print("The combined list is:")
print(combinedList)
