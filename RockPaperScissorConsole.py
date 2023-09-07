import random

gameList = ["rock" , "paper", "scissors"]
youLife = 3
comLife = 3

random.shuffle(gameList)

print("Rock Paper Scissors")
print("You must defeat the computer to win! You both have 3 lives!")
print("Goodluck!")

while True:
    choice = input("\nEnter choice (rock, paper, scissors): ").lower()
    if choice == "rock" or choice == "paper" or choice == "scissors":
        if (gameList[0] == "rock" and choice == "scissors") or (gameList[0] == "scissors" and choice == "paper") or (gameList[0] == "paper" and choice == "rock"):
            print(f"you lose! the computer chose {gameList[0]} and you chose {choice}.")
            youLife -= 1
            random.shuffle(gameList)
        elif choice == gameList[0]:
            random.shuffle(gameList)
            print(f"it's a tie! the computer chose {gameList[0]} and you chose {choice}.")
        else:
            print(f"you win! the computer chose {gameList[0]} and you chose {choice}.")
            comLife -= 1
            random.shuffle(gameList)

        if youLife == 0:
            print("\nYOU LOSE!! GAME OVER!")
            break
        elif comLife == 0:
            print("\nYOU WIN!! CONGRATS!")
            break
    else:
        print("invalid input!")
