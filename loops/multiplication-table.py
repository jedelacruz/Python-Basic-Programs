"""
Multiplication Table:
Description: Create a program that generates the multiplication table of a user-provided number.
Instructions: Use a loop to calculate and print the multiplication table of the given number.
"""

print("Multiplication Table\n")
numAsk = int(input("Enter a number: "))

for number in range(1,16):
    product = numAsk * number
    print(f"{numAsk} x {number} = {product} ")
