"""
Basic Budget Tracker: Create a console-based budget tracker where users can input income and expenses to monitor their finances.
"""
totalExpenses = 0

print("Budget Tracker\n")

while True:
    try:
        incomeAsk = int(input("Enter budget: "))
        income = incomeAsk
        break
    except:
        print("please enter a valid number")


while True:
    expenseAsk = input("Enter expenses (q to quit): ")
    if expenseAsk.lower() == "q":
        break
    else:
        try:
            expenseAsk = int(expenseAsk)
            if expenseAsk > incomeAsk:
                print("you dont have enough budget")
            else:
                incomeAsk -= expenseAsk
                totalExpenses += expenseAsk
        except:
            print("please enter a valid number")

print(f"your income is {income} ₱ and your total expenses is {totalExpenses} ₱")
