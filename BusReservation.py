seats = [0, 0, 0, 0, 0, 0, 0, 0]

while True:

    print("\n===== Bus Reservation System =====")
    print("1. View Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nSeat Status")

        for i in range(len(seats)):
            if seats[i] == 0:
                print("Seat", i + 1, "- Available")
            else:
                print("Seat", i + 1, "- Booked")

    elif choice == "2":

        seat = int(input("Enter seat number: "))

        if seat < 1 or seat > len(seats):
            print("Invalid seat number.")

        elif seats[seat - 1] == 1:
            print("Seat already booked.")

        else:
            seats[seat - 1] = 1
            print("Seat booked successfully.")

    elif choice == "3":

        seat = int(input("Enter seat number to cancel: "))

        if seat < 1 or seat > len(seats):
            print("Invalid seat number.")

        elif seats[seat - 1] == 0:
            print("Seat is already available.")

        else:
            seats[seat - 1] = 0
            print("Booking cancelled.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")