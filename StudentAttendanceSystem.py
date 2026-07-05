students = ["Aman", "Riya", "Rahul", "Sneha", "Arjun"]
attendance = []

while True:

    print("\n===== Student Attendance =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        attendance = []

        print("\nMark Attendance (P/A)\n")

        for name in students:

            status = input(name + ": ").upper()

            while status != "P" and status != "A":
                print("Enter only P or A")
                status = input(name + ": ").upper()

            attendance.append(status)

        print("Attendance Saved Successfully!")

    elif choice == "2":

        if len(attendance) == 0:
            print("Attendance not marked yet.")

        else:

            present = 0

            print("\nAttendance Report")

            for i in range(len(students)):
                print(students[i], "-", attendance[i])

                if attendance[i] == "P":
                    present += 1

            print("\nTotal Present :", present)
            print("Total Absent  :", len(students) - present)

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice")