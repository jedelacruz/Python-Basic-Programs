"""
Simple Login System:
Description: Build a basic login system that asks for a username and password and grants access if they match predefined values.
Instructions: Use if-else statements to compare user inputs with predefined credentials.
"""

# Note: There are many ways to achieve this but im suggesting to use another variable or list to store the credentials

print("School Login System\n")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "Je" and password == "21":
    print("Login Succesfully!")
else:
    print("Invalid Account!")

