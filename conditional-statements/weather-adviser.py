"""
Weather Adviser:
Description: Create a weather advisory program that gives recommendations based on temperature ranges.
Instructions: Use if-elif-else statements to define temperature ranges and suggest appropriate clothing or activities.
"""

print("Weather Adviser\n")
temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("It's very cold. Wear a heavy jacket and stay warm.")
elif temperature >= 0 and temperature < 10:
    print("It's cold. Wear a warm jacket and bundle up.")
elif temperature >= 10 and temperature < 20:
    print("It's cool. A light jacket or sweater should be enough.")
elif temperature >= 20 and temperature < 30:
    print("It's comfortable. T-shirts and light clothing are suitable.")
elif temperature >= 30 and temperature < 40:
    print("It's warm. Wear light clothing and stay hydrated.")
else:
    print("It's hot! Wear light, breathable clothes and stay cool.")
