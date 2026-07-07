cars = []
total = 0

while True:

    print("\n===== Parking System =====")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. View Parked Vehicles")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        number = input("Enter vehicle number: ")
        hours = int(input("How many hours? "))

        fee = hours * 30

        cars.append([number, fee])
        total += fee

        print("Parking Fee: ₹", fee)

    elif choice == "2":

        number = input("Enter vehicle number: ")

        found = False

        for i in range(len(cars)):

            if cars[i][0] == number:
                print("Vehicle Removed")
                cars.pop(i)
                found = True
                break

        if found == False:
            print("Vehicle not found.")

    elif choice == "3":

        if len(cars) == 0:
            print("Parking is empty.")

        else:

            print("\nParked Vehicles")

            for i in range(len(cars)):
                print(cars[i][0], "- ₹", cars[i][1])

            print("Total Collection: ₹", total)

    elif choice == "4":
        print("Closing Parking System...")
        break

    else:
        print("Invalid Choice.")