import random

def start():
    print("ROCK PAPER SCISSORS")
    print()
    mainMenu()

def mainMenu():
    while True:
        print("1. Play")
        print("2. Exit")
        print()
        choiceMainMenu = input(": ")
        print()
        if choiceMainMenu == "1":
            playWindow()
            break
        elif choiceMainMenu == "2":
            break
        else:
            print("Invalid Choice")
            print()

def playWindow():
    while True:
        print("1. Player vs Computer")
        print("2. Player vs Player")
        print()
        playWindowChoice = input(": ")
        print()
        if playWindowChoice == "1":
            playerVScomputer()
            break
        elif playWindowChoice == "2":
            playerVSplayer()
            break
        else:
            print("Invalid Choice")

def playerVScomputer():
    while True:
        print("Player \n1. Rock \n2. Paper \n3. Scissors \n")

        choice = int(input(": "))

        while choice > 3 or choice < 1:
            choice = int(input("Enter valid input: "))

        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        print(": " + choice_name)
        print()
        print("Computer is generating its choice...")

        comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        print("Computer's choice is: " + comp_choice_name)

        print()
        print(choice_name + " V/S " + comp_choice_name)

        result = (choice - comp_choice + 3) % 3

        if result == 0:
            print("Draw")
        elif result == 1:
            print("You win!")
        else:
            print("You lose!")

        print()
        while True:
            print("Do you want to play again? (Y/N)")
            ans = input("\n: ")
            print()
            if ans == 'N' or ans == 'n':
                print("Thanks for playing!")
                print()
                start()
                return
            elif ans == 'Y' or ans == 'y':
                print('Play again')
                print()
                break
            else:
                print("Invalid")
                print()


def playerVSplayer():
    while True:
        print("Player 1")
        play1Choice = input("1.Rock \n2.Paper \n3.Scissors \n\n: ")

        print()

        print("Player 2")
        play2Choice = input("1.Rock \n2.Paper \n3.Scissors \n\n: ")

        print()

        if play1Choice == "1" and play2Choice == "1":
            print("Draw")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "1" and play2Choice == "2":
            print("Player 2 won!")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "1" and play2Choice == "3":
            print("Player 1 won!")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "2" and play2Choice == "1":
            print("Player 1 won!")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "2" and play2Choice == "2":
            print("Draw")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "2" and play2Choice == "3":
            print("Player 2 won!")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "3" and play2Choice == "1":
            print("Player 2 won!")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "3" and play2Choice == "2":
            print("Player 1 won!")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        elif play1Choice == "3" and play2Choice == "3":
            print("Draw")
            print()
            while True:
                print("Do you want to play again? (Y/N)")
                ans = input("\n: ")
                print()
                if ans == 'N' or ans == 'n':
                    print("Thanks for playing!")
                    print()
                    start()
                    return
                elif ans == 'Y' or ans == 'y':
                    print('Play again')
                    print()
                    break
                else:
                    print("Invalid")
                    print()
        else:
            print("Invalid")
            print()


start()
