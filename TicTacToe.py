board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

player = "X"


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_win():
    if board[0] == board[1] == board[2] != " ":
        return True
    if board[3] == board[4] == board[5] != " ":
        return True
    if board[6] == board[7] == board[8] != " ":
        return True
    if board[0] == board[3] == board[6] != " ":
        return True
    if board[1] == board[4] == board[7] != " ":
        return True
    if board[2] == board[5] == board[8] != " ":
        return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True

    return False


count = 0

while count < 9:

    print_board()

    pos = int(input("Player " + player + " Enter position (1-9): "))

    if board[pos - 1] == " ":
        board[pos - 1] = player
        count += 1
    else:
        print("Already Filled!")
        continue

    if check_win():
        print_board()
        print("Player", player, "Wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

if count == 9 and not check_win():
    print_board()
    print("Match Draw!")