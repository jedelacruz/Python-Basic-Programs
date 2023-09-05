taskList = []

def main():
    print("Task List Manager\n")
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")
        print()

        try:
            menuChoice = int(input("Enter a choice: "))
            print()
            if menuChoice == 1:
                addTaskSec()
            elif menuChoice == 2:
                viewTaskSec()
            elif menuChoice == 3:
                deleteTaskSec()
            elif menuChoice == 4:
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid choice. Please enter a number.")
        print()


def addTaskSec():
    print("----- Add Task -----\n")
    while True:
        askUser = input("Enter task (or press Enter to return to the main menu): ")
        print()
        if not askUser:
            print("Returning to the main menu.")
            print()
            break
        else:
            taskList.append(askUser)
            print("Task added successfully.")
            print()

def viewTaskSec():
    print("----- View Tasks -----\n")
    if not taskList:
        print("No tasks available.")
    else:
        for index, task in enumerate(taskList, start=1):
            print(f"{index}. {task}")
    print()

def deleteTaskSec():
    print("----- Delete Task -----\n")
    viewTaskSec()
    if not taskList:
        print("Task list is empty.")
        return

    while True:
        try:
            deleteAsk = int(input("Enter the number of the task to delete (or press Enter to return to the main menu): "))
            print()
            if 1 <= deleteAsk <= len(taskList):
                deleted_task = taskList.pop(deleteAsk - 1)
                print(f"Task '{deleted_task}' deleted successfully.")
                break
            elif not deleteAsk:
                print("Returning to the main menu.\n")
                break
            else:
                print("Invalid task number. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
