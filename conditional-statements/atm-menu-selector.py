"""
Menu Selector:
Description: Build a program that displays a menu of options and performs actions based on user selections.
Instructions: Use a loop to display the menu repeatedly. Use if-elif-else statements to execute the selected action.
"""

import random

randomNumber = random.randint(100, 999)
cash = 1000

def main():
    print("Welcome to ATM\n")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    welcomeChoice = int(input("Choice: "))
    if welcomeChoice == 1:
        loginPage()
    elif welcomeChoice == 2:
        registerPage()
    elif welcomeChoice == 3:
        print("Thanks for using!")
        exit()
    else:
        print("Wrong input!\n")
        main()

def loginPage():
    pinAsk = int(input("Please Enter Your Pin: "))
    if pinAsk == randomNumber:
        print("Login Succesfuly\n")
        succesfulLogin()
    else:
        print("Invalid Account\n")
        main()

def registerPage():
    print("\n")
    print("Your pin is ", randomNumber)
    print("Thanks for registering\n")
    main()

def succesfulLogin():
    global cash
    print("----------------------------- ATM -----------------------------")
    print("1. View Cash")
    print("2. Deposit Cash")
    print("3. Withdraw Cash")
    print("4. Logout")
    menuChoice = int(input("Choice: "))
    if menuChoice == 1:
        print("Cash: ", cash)
        print("\n")
        succesfulLogin()
    elif menuChoice == 2:
        depositCash = int(input("Deposit Cash: "))
        cash += depositCash
        print("\n")
        succesfulLogin()
    elif menuChoice == 3:
        depositCash = int(input("Withdraw Cash: "))
        if depositCash > cash:
            print("Not Enough Cash in Account")
            succesfulLogin()
        else:
            cash -= depositCash
            print("\n")
            succesfulLogin()
    elif menuChoice == 4:
        print("\n")
        main()
    else:
        print("Invalid Choice")
        succesfulLogin()

main()
