import random

players = []

while True:

    print("\n===== Lucky Draw =====")
    print("1. Add Participant")
    print("2. View Participants")
    print("3. Pick Winner")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter participant name: ")
        players.append(name)
        print("Participant Added!")

    elif choice == "2":

        if len(players) == 0:
            print("No participants yet.")

        else:
            print("\nParticipants")

            for i in range(len(players)):
                print(i + 1, ".", players[i])

    elif choice == "3":

        if len(players) == 0:
            print("No participants available.")

        else:
            winner = random.choice(players)

            print("\n🎉 Winner is:", winner)

    elif choice == "4":

        print("Program Ended.")
        break

    else:

        print("Invalid Choice.")