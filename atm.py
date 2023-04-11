#ATM
#This is just a test program, it has no functions

print()
print("================ Lyceum ATM ================")
print()
pin = 12345
pinGuess = int(input("Enter your pin: "))
if (pinGuess == pin):
    print("Succesfuly Login")
    print()
    print("================ Lyceum ATM ================")
    print()
    print("Type the number of your transaction")
    print()
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check balance")
    print("4.Account settings")
    print("5.Logout")
    print()
    choice = int(input("Enter the number of your choice: "))
    if(choice == 1):
        print("Withdrawing money...")
    elif(choice == 2):
        print("Depositing money...")
    elif (choice == 3):
        print("Checking balance...")
    elif (choice == 4):
        print("Managing account settings...")
    elif (choice == 5):
        print("Logging out...")
    else:
        print("Invalid number, Please try again.")
else:
    print("Account doesn't exist")
