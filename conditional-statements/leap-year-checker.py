"""
Leap Year Checker:
Description: Develop a program that checks if a given year is a leap year or not.
Instructions: Use if-else statements to check if the year is divisible by 4 and not divisible by 100, or if it's divisible by 400.
"""

print("Leap Year Checker\n")
yearAsk = int(input("Enter year: "))

if yearAsk % 400 == 0:
    print(f"{yearAsk} is a Leap Year")
else:
    print(f"{yearAsk} is not a Leap Year")

