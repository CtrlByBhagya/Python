expenses = []
total = 0

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        item = input("What did you spend on? ")
        amount = float(input("Enter amount: "))

        expenses.append([item, amount])
        total = total + amount

        print("Expense added successfully.")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses added yet.")

        else:
            print("\nYour Expenses:")
            for i in range(len(expenses)):
                print(i + 1, ".", expenses[i][0], "-", expenses[i][1])

    elif choice == "3":

        print("Total Expense =", total)

    elif choice == "4":

        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")