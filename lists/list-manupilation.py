"""
11. List Manipulation:
Write a program that takes two lists as input and creates a new list containing common elements between the two input lists.
"""

list1 = []
list2 = []
list3 = []

while True:
    askList1 = input("Enter element to list1 (q to quit): ")
    if askList1.lower() == "q":
        break
    else:
        list1.append(askList1)

while True:
    askList2 = input("Enter element to list2 (q to quit): ")
    if askList2.lower() == "q":
        break
    else:
        list2.append(askList2)

for element in list1:
    if element in list2:
        list3.append(element)

print("List 1 elements:")
print(list1)

print()

print("List 2 elements:")
print(list2)

print()

print("Common Elements of L1 and L2")
print(list3)
