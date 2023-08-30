"""
print odd number using while loop
"""

askNum = int(input("Enter a num: "))
i = 1
while i <= askNum:
    if i % 2 != 0:
        print(i)
    i+=1
