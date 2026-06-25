import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("\nRock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer:", computer)

    if user == computer:
        print("Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score: You {user_score} - {computer_score} Computer")

    if input("Play again? (y/n): ").lower() != "y":
        break

print("\nFinal Score")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")