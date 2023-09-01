cart = []
total = 0

while True:
    askGrocery = input("Enter grocery (q to quit): ")
    if askGrocery == "q" or askGrocery == "Q":
        break
    else:
        while True:
            try:
                askPrice = int(input("Enter price: "))
                total += askPrice
                cart.append((askGrocery, askPrice))  
            except ValueError:
                print("Invalid Input. Please type a number!")
            else:
                break

for item in cart:
    print(f"Grocery: {item[0]}, Price: {item[1]}")

print(f"Total: {total}")
