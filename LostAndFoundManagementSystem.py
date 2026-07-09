items = []

while True:

    print("\n===== Lost & Found =====")
    print("1. Add Lost Item")
    print("2. View Lost Items")
    print("3. Claim Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        item = input("Enter item name: ")
        place = input("Where was it found? ")

        items.append([item, place])

        print("Item added successfully.")

    elif choice == "2":

        if len(items) == 0:
            print("No items available.")

        else:

            print("\nLost Items")

            for i in range(len(items)):
                print(i + 1, ".", items[i][0], "-", items[i][1])

    elif choice == "3":

        item = input("Enter item name to claim: ")

        found = False

        for i in range(len(items)):

            if items[i][0].lower() == item.lower():
                items.pop(i)
                found = True
                print("Item claimed successfully.")
                break

        if found == False:
            print("Item not found.")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice.")