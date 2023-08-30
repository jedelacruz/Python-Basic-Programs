import random
import time

randomNum = random.randint(1,20)
countGuess = 1
lives = 5

print("--------------------- Guess the Lucky Number ---------------------\n")
time.sleep(2)
input("You only have 5 lives, Are you brave enough to guess the lucky number? ")
print()

while True:
    try:
        while True:
            guessNum = int(input("Guess the lucky number: "))
            if guessNum == randomNum:
                print("You win! The lucky number is", randomNum)
                print(f"You guessed {countGuess} times")
                break
            elif guessNum > randomNum:
                print("You were above the number!")
                countGuess += 1
                lives -= 1
                if lives == 0:
                    print("You lose! The lucky number is", randomNum)
                    break
            elif guessNum < randomNum:
                print("You were below the number!")
                countGuess += 1
                lives -= 1
                if lives == 0:
                    print("You lose! The lucky number is", randomNum)
                    break

    except ValueError:
        print("please type an integer")
    else:
        break
    
