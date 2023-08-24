"""
Guess the Number Game (Limited Tries):
Description: Implement a guessing game where the user tries to guess a randomly generated number within a limited number of tries.
Instructions: Use a loop to provide a certain number of attempts for the user to guess.
"""
import random

random_number = random.randint(1,10)

print("Guess the number\n")

for i in range(3):
    numAsk = int(input("Enter a number(1-10): "))
    if numAsk == random_number:
        print("You win! The number is", random_number)
        break
    else:
        print("Keep Guessing!")
        continue
else:
    print("You lose! The number is", random_number)
