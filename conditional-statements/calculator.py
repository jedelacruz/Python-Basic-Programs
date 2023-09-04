# simple calculator

firstNum = int(input("Enter the first num: "))
secondNum  = int(input("Enter the second num: "))
operator = input("Enter the operation (+ , - , * , /): ")

if operator == "+":
    result = firstNum + secondNum
elif operator == "-":
    result = firstNum - secondNum
elif operator == "*":
    result = firstNum * secondNum
elif operator == "/":
    result = firstNum / secondNum
else:
    print("Invalid Operator")

print(result)
