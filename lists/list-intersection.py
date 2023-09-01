"""
13. List Intersection:
Write a program that takes two lists as input and creates a new list containing elements that are common between the two input lists (intersection).
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

for i in list1:
    if i in list2:
        list3.append(i)

print(list3)
