# to do app

list = []

print("To do App")

def main():

    print("1. View List")
    print("2. Add")
    print("3. Delete")
    print("4. Exit")
    choice = int(input(": "))

    if(choice == 1):
        print(list)
        main()
    elif(choice == 2):
        task = input("Enter text you want to add: ")
        list.append(task)
        main()
    elif(choice == 3):
        deleteTask = int(input("Enter the index/number you want to delete.(starts at 0) :"))
        list.pop(deleteTask)
        main()
    elif(choice == 4):
        print("Thanks for using!")
        exit()
    else:
        print("Invalid choice!")
        main()
main()
