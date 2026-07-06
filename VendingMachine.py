chips = 20
cold_drink = 35
chocolate = 25
biscuits = 15

total = 0

while True:

    print("\n===== VENDING MACHINE =====")
    print("1. Chips - ₹20")
    print("2. Cold Drink - ₹35")
    print("3. Chocolate - ₹25")
    print("4. Biscuits - ₹15")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        total = total + chips
        print("Chips added.")

    elif choice == "2":
        total = total + cold_drink
        print("Cold Drink added.")

    elif choice == "3":
        total = total + chocolate
        print("Chocolate added.")

    elif choice == "4":
        total = total + biscuits
        print("Biscuits added.")

    elif choice == "5":
        print("\nTotal Bill = ₹", total)

        money = int(input("Enter amount paid: "))

        if money >= total:
            print("Change =", money - total)
            print("Thank you for your purchase!")
            total = 0
        else:
            print("Insufficient money!")

    elif choice == "6":
        print("Machine Closed.")
        break

    else:
        print("Invalid Choice.")