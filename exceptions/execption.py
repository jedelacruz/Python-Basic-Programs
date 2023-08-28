while True:
    try:
        x = int(input("Enter x: "))
    except ValueError:
        #print("please type a number")
        pass
    else:
        break

print(f"x is {x}")
