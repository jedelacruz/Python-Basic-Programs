"""
Write a Python program that takes a string as input and prints the string in reverse order and loop it.
"""

ask = input("Enter a word: ")
loop = int(input("Enter how many times to loop: "))

for _ in range(loop):
    print(ask[::-1])
