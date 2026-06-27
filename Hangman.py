word = "python"
guessed = ""

attempts = 6

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("🎉 You Won!")
        break

    guess = input("Guess a letter: ")

    if guess in word:
        guessed += guess
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Game Over!")
    print("Word was:", word)