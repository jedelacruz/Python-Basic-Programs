"""
Print Odd Numbers:
Description: Create a program that prints all odd numbers from 1 to a user-provided limit.
Instructions: Use a loop to iterate through numbers and print odd ones.
"""

print("Odd Numbers\n")
askNum = int(input("Enter a number: "))

for i in range(1, askNum + 1):
    if i % 2 != 0:
        print(i)
