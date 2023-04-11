#vending machine

def start():
    print("============= 1 DOLLAR VENDING MACHINE =============")
    print()
    menu()

def menu():
    print("1. Granola Bars")
    print("2. Doritos")
    print("3. Pretzels")
    print("4. Bubble Gum")
    print("5. Coke")
    print("6. Sprite")
    print("7. Gatorade")
    print("8. Bottled Water")
    print("0. Exit")
    print()
    menuChoice()

def menuChoice():
    while True:
        coin = input("Pick your order: ")

        if coin == "1":
            print("Order: Granola Bars")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Granola Bars")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "2":
            print("Order: Doritos")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Doritos")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "3":
            print("Order: Pretzels")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Pretzels")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "4":
            print("Order: Bubble Gum")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Bubble Gum")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "5":
            print("Order: Coke")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Coke")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "6":
            print("Order: Sprite")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Sprite")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "7":
            print("Order: Gatorade")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Gatorade")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "8":
            print("Order: Bottled Water")
            while True:
                coinSure = input("Are you sure this is your order? (y/n): ")
                if coinSure == "y":
                    payment()
                    print("Order Sent: Bottled Water")
                    print()
                    print("Thank you for Ordering!")
                    return
                elif coinSure == "n":
                    print()
                    break
                else:
                    print("Invalid text")
                    print()

        elif coin == "0":
            break

def payment():
    while True:
        insertCoin = int(input("Insert your money: "))
        if insertCoin == 1:
            print("Change: 0")
            break
        elif insertCoin < 1:
            print("Not enough")
        elif insertCoin > 1:
            result = insertCoin - 1
            print("Change: " + str(result))
            break
start()
