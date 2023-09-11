priceList = []
itemList = []

def main():
    print("Shopping Cart List\n")
    while True:
        askItem = input("Enter item (q to quit): ")
        if askItem.lower() == "q":
            final()
            break
        else:
            itemList.append(askItem)
            while True:
                try:
                    askPrice = int(input("Enter price: "))
                    priceList.append(askPrice)
                    break
                except ValueError:
                    print("please enter a valid price")

def final():
    print("\nItem Lists\n")
    total = 0
    for i in range(len(itemList)):
        print(f"{itemList[i]:<10} : {priceList[i]}₱")
        total += priceList[i]
    
    print()
    print(f"Total{'':<6}: {total}₱")

main()
