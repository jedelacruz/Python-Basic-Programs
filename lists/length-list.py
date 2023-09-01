"""
9. List Length:
Write a program that calculates and prints the length of a given list.
"""

list = []

while True:
    askUser = input("Enter x (press q to quit):  ")
    if askUser.lower() == "q":
        break
    else:
        list.append(askUser)

getLength = len(list)

print("The length of list is", getLength)
