import random

randomNumber = random.randint(0,5)

guessNumber = int(input("Guess the number between 1-5: "))

if(guessNumber == randomNumber):
    print("Congrats bro! You win!")
else:
    print(f"You lose! The number is {randomNumber}")
