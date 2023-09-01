"""
6. List Filtering:
Write a program that takes a list of numbers as input and creates a new list containing only the positive numbers.
"""

list = []
positive_list = []

while True:
    askInput = input("Enter a number (press q if you're done): ")

    if askInput.lower() == "q":
        break
    else:
        try:
            number = int(askInput)
            list.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q'.")

for num in list:
    if num > 0:
        positive_list.append(num)

for num in positive_list:
    print(num)



