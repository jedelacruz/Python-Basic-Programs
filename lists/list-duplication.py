"""
5. List Duplication:
Write a program that takes a list as input and creates a new list containing each element duplicated.
"""

list = []
duplicatedList = []

while True:
    askUser = input("Enter x (q to quit): ")
    if askUser == "q" or askUser == "Q":
        break
    else:
        list.append(askUser)

duplicatedList.append(list)

print("The list is:")
print(list)

print()

print("The duplicated list is: ")
for i in duplicatedList:
    print(i, end="")
