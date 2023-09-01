"""
10. List Element Search:
Write a program that takes a list and a target element as input and checks if the target element is present in the list.
"""

list = []

while True:
    askUserList = input("Enter number to list (q to quit): ")
    if askUserList.lower() == "q":
        break
    else:
        try:
            int(askUserList)
            list.append(askUserList)
        except ValueError:
            print("Only type numbers or 'q'")

askUserFind = input("Enter number to find: ")
if askUserFind in list:
    print(f"{askUserFind} is in the list")
else:
    print(f"The {askUserFind} isn't on this list.")
