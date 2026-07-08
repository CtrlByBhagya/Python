balance = 0

while True:

    print("\n====== Mobile Recharge ======")
    print("1. Check Balance")
    print("2. Add Money")
    print("3. Recharge Pack")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("Wallet Balance: ₹", balance)

    elif choice == "2":

        amount = int(input("Enter amount: "))
        balance += amount
        print("Money Added Successfully!")

    elif choice == "3":

        print("\nAvailable Packs")
        print("1. ₹199")
        print("2. ₹299")
        print("3. ₹499")

        pack = input("Select Pack: ")

        if pack == "1":
            price = 199
        elif pack == "2":
            price = 299
        elif pack == "3":
            price = 499
        else:
            print("Invalid Pack")
            continue

        if balance >= price:
            balance -= price
            print("Recharge Successful!")
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance.")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")