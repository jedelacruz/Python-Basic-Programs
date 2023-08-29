import time
from colorama import Fore, Back, Style

score = 0
mins = 0

def main():
    global score

    print("------------------- QUIZ GAME -------------------\n")
    name = input("Enter your name: ")
    print()
    print(f"Hello {name}!\nType to answer\nGoodluck!")
    time.sleep(3)

    print()
    print("Ready")
    time.sleep(1)
    print("Set")
    time.sleep(1)
    print("Go!")
    print()

    while True:
        try:
            q1 = int(input("1. How many days does the Earth have? "))
            if q1 == 365:
                print(Fore.GREEN + "Correct Answer!")
                score += 1
            else:
                print(Fore.RED + "Wrong Answer!")
            
            print(Style.RESET_ALL)

            q2 = int(input("2. How many moon does the Earth have? "))
            if q2 == 1:
                print(Fore.GREEN + "Correct Answer!")
                score += 1
            else:
                print(Fore.RED + "Wrong Answer!")
            
            print(Style.RESET_ALL)

            q3 = int(input("3. How many colors are in a panda? "))
            if q3 == 2:
                print(Fore.GREEN + "Correct Answer!")
                score += 1
            else:
                print(Fore.RED + "Wrong Answer!")
            
            print(Style.RESET_ALL)

            q4 = int(input("4. How many seasons are there in tropical countries? "))
            if q4 == 2:
                print(Fore.GREEN + "Correct Answer!")
                score += 1
            else:
                print(Fore.RED + "Wrong Answer!")
            
            print(Style.RESET_ALL)

            print(Fore.GREEN +"BONUS!")
            score += 1

            print(Style.RESET_ALL)

            endGame(name,score)

        except ValueError:
            pass
        else:
            break

def endGame(player_name,player_score):
    if player_score <= 2:
        print(f"Hello {player_name}! You scored {player_score}/5! That's" + Fore.RED + " terrible!")
        print(Style.RESET_ALL)
    elif player_score == 3:
        print(f"Hello {player_name}! You scored {player_score}/5! That's" + Fore.YELLOW + " mid!")
        print(Style.RESET_ALL)
    elif player_score > 3:
        print(f"Hello {player_name}! You scored {player_score}/5! That's" + Fore.GREEN + " great!")
        print(Style.RESET_ALL)


main()
