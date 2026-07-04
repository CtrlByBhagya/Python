candidates = ["Alice", "Bob", "Charlie"]
votes = [0, 0, 0]

while True:

    print("\n===== Voting System =====")
    print("1. Cast Vote")
    print("2. View Result")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nCandidates")

        for i in range(len(candidates)):
            print(i + 1, ".", candidates[i])

        vote = int(input("Vote for candidate (1-3): "))

        if vote >= 1 and vote <= len(candidates):
            votes[vote - 1] += 1
            print("Vote recorded successfully.")
        else:
            print("Invalid candidate.")

    elif choice == "2":

        print("\nElection Result")

        for i in range(len(candidates)):
            print(candidates[i], ":", votes[i], "votes")

        highest = max(votes)
        winner = votes.index(highest)

        print("Winner is", candidates[winner])

    elif choice == "3":
        print("Voting Closed.")
        break

    else:
        print("Invalid choice.")