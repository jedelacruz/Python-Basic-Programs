#a program that will ask the user to type a word then prompt the user
#if it wants to display the text in (1) capital letters or (2) small letters.

while True:
    word = input("Enter a word: ")
    choice = int(input("Do you want to display the text in (1) Capital or (2) Small: "))

    if choice == 1:
        print(word.upper())
    elif choice == 2:
        print(word.lower())
    else:
        print("Invalid")

    repeat = input("Do you want to use the program again? (yes/no) ")
    if repeat.lower() == "no":
        break
