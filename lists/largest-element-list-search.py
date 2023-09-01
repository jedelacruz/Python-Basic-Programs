"""
10. List Element Search:
Write a program that takes a list and a target element as input and checks if the target element is present in the list.
"""
list = []

print("Largest Number in a list")
print()

while True:
    askUser = input("Enter a number(press q to quit): ")
    if askUser.lower() == "q":
        break
    else:
        list.append(askUser)

largest_num = max(list)

print(f"The list is:\n{list}")
print(f"The largest number in the list is {largest_num}")
