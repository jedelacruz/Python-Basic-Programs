"""
7. List Sorting:
Write a program that sorts a list of numbers in descending order and prints the sorted list.
"""

list = [3,-32,102,31,63]

sortedList = reversed(sorted(list))

print("List:")
for i in list:
    print(i)

print()

print("Descending Sorted List:")
for i in sortedList:
    print(i)
