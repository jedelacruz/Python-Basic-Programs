degreeChoice = int(input("(1) - Convert C to F\n(2) - Convert F to C\nChoice: "))

if degreeChoice == 1:
    celciusChoice = int(input("Enter Celsius: "))
    celciusChoiceResult = celciusChoice * 1.8 + 32
    print(f"The converted value is {celciusChoiceResult} Fahrenheit.")
elif degreeChoice == 2:
    fahrenheitChoice = int(input("Enter Fahrenheit: "))
    fahrenheitChoiceResult = (fahrenheitChoice - 32) * 5/9
    print(f"The converted value is {fahrenheitChoiceResult} Celsius.")
else:
    print("Invalid Choice.")
