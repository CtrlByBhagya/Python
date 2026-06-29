tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
        else:
            print("Invalid task number.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")