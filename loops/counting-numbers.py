"""
Counting Numbers:
Description: Write a program that counts and prints numbers from 1 to a user-provided limit.
Instructions: Use a while loop or a for loop to iterate through the numbers and print each one.
"""

print("Counting Numbers\n")
numAsk = int(input("Enter a number: "))

for i in range(numAsk):
    i += 1
    print(i)
