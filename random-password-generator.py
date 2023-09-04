import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]|;:'<>,.?/"

pwLength = int(input("Enter how many characters: "))
password = ""

for i in range(pwLength):
    password += random.choice(characters)

print("your password is", password)
