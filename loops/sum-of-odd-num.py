"""
Write a Python program that calculates and prints the odd of all even numbers from 1 to a given positive integer n.
"""

askNum = int(input("Enter a number: "))

for i in range(1,askNum+1):
    if i % 2 != 0:
        print(i)
    
