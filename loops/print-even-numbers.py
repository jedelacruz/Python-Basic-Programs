"""
Print Even Numbers:
Description: Write a program that prints all even numbers from 1 to a user-provided limit.
Instructions: Use a loop to iterate through numbers and print even ones.
"""

print("Even Numbers\n")
askNum = int(input("Enter a number: "))

for i in range(1, askNum + 1):
    if i % 2 == 0:
        print(i)
