while True:
    number = "9"
    numberGuess = input("Guess the number: ")
    if numberGuess == number:
        print("You win!")
        break
    else:
        print("You lose!")
