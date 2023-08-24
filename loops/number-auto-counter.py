"""
Will ask the user for 2 numbers
- first (start num)
- second (end num)
"""

print("Number Counter\n")
firstNum = int(input("Enter start number: "))
secondNum = int(input("Enter end number: "))

for i in range(firstNum -1,secondNum):
    i += 1
    print(i)
