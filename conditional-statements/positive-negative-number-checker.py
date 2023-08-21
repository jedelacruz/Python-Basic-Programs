"""
Positive/Negative Number Identifier:
Description: Build a program that determines if a number is positive, negative, or zero.
Instructions: Use if-elif-else statements to check the sign of the number and print the appropriate message.
"""

print("Positive/Negative Checker\n")

askNumber = int(input("Enter a number:"))

if askNumber == 0:
    print("The number is a 0")
elif askNumber > 0:
    print("The number is a positive")
else:
    print("The number is negative")
