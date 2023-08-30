"""
Write a Python program that checks if a given positive integer n is a prime number.
"""
askUser = input("Enter a word: ")

if askUser[::-1] == askUser:
    print(askUser, "is a palindrome")
else:
    print(askUser, "is not a palindrome")
