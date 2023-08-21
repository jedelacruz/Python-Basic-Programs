"""
Age Classifier:
Description: Create a program that takes a person's age as input and classifies them as a child, teenager, or adult.
Instructions: Use if-elif-else statements to define the age ranges and print appropriate messages.
"""

print("Age Classifier\n")

ageAsk = int(input("Enter your age: "))

if ageAsk > 0 and ageAsk <= 13:
    print(f"{ageAsk}, You are a child")
elif ageAsk >= 14 and ageAsk <= 18:
    print(f"{ageAsk}, You are a teenager")
else:
    print(f"{ageAsk}, You are an adult")
