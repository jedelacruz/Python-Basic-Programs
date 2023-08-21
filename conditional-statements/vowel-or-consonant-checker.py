"""
Vowel or Consonant Checker:
Description: Write a program that checks if a given letter is a vowel or a consonant.
Instructions: Use if-elif-else statements to identify vowels and print corresponding messages.
"""

print("Vowel or Consonant Checker\n")

askLetter = input("Enter a letter: ").lower()

if askLetter == "a" or askLetter == "e" or askLetter == "i" or askLetter == "o" or askLetter == "u":
    print(f"{askLetter} is a vowel")
else:
    print(f"{askLetter} is a consonant")
