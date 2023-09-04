"""
Contact Book: Build a console application for managing contacts. Users can add, view, update, and delete contact information.
"""

contactList = {}
keys = contactList.keys()
values = contactList.values()

def main():
    print("Contact Book\n")

    print("1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print()

    while True:
        try:
            menuChoice = int(input("Enter choice: "))
            print()

            if menuChoice == 1:
                addSection()
            elif menuChoice == 2:
                viewSection()
            elif menuChoice == 3:
                updateSection()
            elif menuChoice == 4:
                deleteSection()

        except:
            pass
            print()
    
def addSection():
    addAskName = input("Enter contact name: ")
    try:
        addAskContact = int(input("Enter contact number: "))
    except ValueError:
        print("please enter a valid number")
    contactList[addAskName] = addAskContact
    print()
    main()
def viewSection():
    for index, (name, contact) in enumerate(contactList.items(), start=1):
        print(f"{index}. {name} - {contact}")
    print()
    main()
def updateSection():
    updateAskName = input("Enter the contact name: ")
    try:
        updateNewNumber = int(input("Enter new contact number: "))
    except ValueError:
        print("please enter a valid number")

    if updateAskName in contactList:
        contactList.update({updateAskName:updateNewNumber})
        print("contact updated succesfuly")
    else:
        print()
        print("contact name not found")
    print()
    main()
def deleteSection():
    deleteAskName = input("Enter the contact name: ")
    if deleteAskName in contactList:
        contactList.pop(deleteAskName)
        print("contact deleted succesfully")
    else:
        print()
        print("contact name not found")
    print()
    main()

main()

