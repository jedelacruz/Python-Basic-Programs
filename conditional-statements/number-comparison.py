"""
Number Comparison:
Description: Write a program that compares two numbers and determines if one is greater, smaller, or equal to the other.
Instructions: Use if-elif-else statements to compare the numbers and print the appropriate message.
"""

print("Number Compare\n")

numberAsk1 = int(input("Enter first number: "))
numberAsk2 = int(input("Enter second number: "))

if numberAsk1 > numberAsk2:
    print(f"{numberAsk1} is greater than {numberAsk2}")
elif numberAsk1 == numberAsk2:
    print(f"{numberAsk1} is equal to {numberAsk2}")
else:
    print(f"{numberAsk2} is greater than {numberAsk1}")
