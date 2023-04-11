print("*********** 2 Player Rock Paper Scissors ***********")
print()

while True:
    print("Player 1")
    play1Choice = input("1.Rock \n2.Paper \n3.Scissors \n")

    print()

    print("Player 2")
    play2Choice = input("1.Rock \n2.Paper \n3.Scissors \n")

    if play1Choice == "1" and play2Choice == "1":
        print("Draw")
        break
    elif play1Choice == "1" and play2Choice == "2":
        print("Player 2 won!")
        break
    elif play1Choice == "1" and play2Choice == "3":
        print("Player 1 won!")
        break
    elif play1Choice == "2" and play2Choice == "1":
        print("Player 1 won!")
        break
    elif play1Choice == "2" and play2Choice == "2":
        print("Draw")
        break
    elif play1Choice == "2" and play2Choice == "3":
        print("Player 2 won!")
        break
    elif play1Choice == "3" and play2Choice == "1":
        print("Player 2 won!")
        break
    elif play1Choice == "3" and play2Choice == "2":
        print("Player 1 won!")
        break
    elif play1Choice == "3" and play2Choice == "3":
        print("Draw")
        break
    else:
        print("Invalid")
        print()
