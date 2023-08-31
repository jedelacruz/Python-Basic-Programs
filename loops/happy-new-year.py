import time

askNum = int(input("Enter a number: "))
for i in reversed(range(1,askNum+1)):
    print(i)
    time.sleep(1)

print("Happy New Year!")
