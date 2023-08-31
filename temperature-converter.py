print("Temperature Converter")
print()
print("Please type 'C' to convert Celcius to Farenheit")
print("Please type 'F' to convert Farenheit to Celcius")

while True:
    convertAsk = input(": ").upper()
    if convertAsk == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        break
    elif convertAsk == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid Input")
