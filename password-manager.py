import random

passwordList = {}

def main():
    print("------------------- Password Manager -------------------\n")
    print("1. View Password")
    print("2. Add Password")
    print("3. Update Password")
    print("4. Delete Password")
    print("5. Generate Random Password")
    print("6. Exit")
    print()

    while True:
        try:
            menuChoice = int(input("Enter choice: "))
            print()
            if menuChoice == 1:
                viewPW()
                break
            elif menuChoice == 2:
                addPW()
                break
            elif menuChoice == 3:
                updatePW()
                break
            elif menuChoice == 4:
                deletePW()
                break
            elif menuChoice == 5:
                generatePW()
                break
            elif menuChoice == 6:
                print("thanks for using!")
                break
        except ValueError:
            print("invalid choice")
            print()

def viewPW():
    print("------------- View Password -------------")
    print()
    if not passwordList:
        print("no password found")
    else:
        print("Passwords:\n")
        for i,y in passwordList.items():
            print(f"{i} : {y}")
    print()
    main()

def addPW():
    print("------------- Add Password --------------")
    print()
    pwName = input("Enter password name: ")
    pwPassword = input("Enter password: ")
    passwordList[pwName] = pwPassword
    print()
    print("password added succesfuly")
    print()
    main()

def updatePW():
    print("------------ Update Password ------------")
    print()
    updatePwName = input("Enter password name: ")
    updatePWpass = input("Enter new password: ")

    if updatePwName in passwordList:
        passwordList.update({updatePwName: updatePWpass})
        print()
        print("password updated succesfuly")
    else:
        print()
        print("password name not found")
    print()
    main()

def deletePW():
    print("------------ Delete Password ------------")
    print()
    deletePwName = input("Enter password name: ")
    if deletePwName in passwordList:
        passwordList.pop(deletePwName)
        print()
        print("password deleted succesfuly")
    else:
        print()
        print("password name not found")
    print()
    main()
    
def generatePW():
    print("----------- Generate Password -----------")
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]|;:'<>,.?/"
    
    while True:
        try:
            print()
            pwLength = int(input("Enter how many characters: "))
            break
        except:
            print("please enter a number")
    password = ""

    for i in range(pwLength):
        password += random.choice(characters)

    print("the generated password is", password)
    print()
    main()
    
main()
