seats = ["Empty"] * 10

while True:

    print("\n===== Movie Ticket Booking =====")
    print("1. Show Seats")
    print("2. Book Seat")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nSeat Status")

        for i in range(10):
            print("Seat", i + 1, "-", seats[i])

    elif choice == "2":

        seat = int(input("Enter seat number (1-10): "))

        if seat < 1 or seat > 10:
            print("Invalid seat number.")

        elif seats[seat - 1] == "Booked":
            print("Seat already booked.")

        else:
            seats[seat - 1] = "Booked"
            print("Booking successful.")

    elif choice == "3":

        seat = int(input("Enter seat number to cancel: "))

        if seat < 1 or seat > 10:
            print("Invalid seat number.")

        elif seats[seat - 1] == "Empty":
            print("Seat is already empty.")

        else:
            seats[seat - 1] = "Empty"
            print("Booking cancelled.")

    elif choice == "4":

        print("Thank you!")
        break

    else:
        print("Invalid choice.")