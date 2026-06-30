contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Phone Number: ")
        contacts[name] = number

    elif choice == "2":
        for name in contacts:
            print(name, ":", contacts[name])

    elif choice == "3":
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        break