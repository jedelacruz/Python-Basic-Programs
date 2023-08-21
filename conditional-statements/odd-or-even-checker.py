"""
Odd or Even Checker:
Description: Create a program that checks whether a given number is odd or even.
Instructions: Use the modulo operator (%) to check if a number is divisible by 2. Print the result using if-else statements.
"""

print("Odd or Even Checker\n")

numberAsk = int(input("Enter a number: "))
if numberAsk % 2 == 0:
    print(f"{numberAsk} is even number.")
else:
    print(f"{numberAsk} is odd number.")
