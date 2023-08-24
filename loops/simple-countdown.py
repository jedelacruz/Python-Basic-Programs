"""
Simple Countdown:
Description: Develop a program that counts down from a user-provided number to 1 and prints each number.
Instructions: Use a loop to iterate in reverse and print the numbers.
"""
import time

print("Countdown Timer\n")
askNum = int(input("Enter a number: "))
for i in range(askNum):
    askNum -= 1
    print(askNum + 1)
    time.sleep(1)

print("Happy New Year!!!!")
