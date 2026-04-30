board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
current_player = "X"
def print_board():
    for row in board:
        print(*row)
def check_win(player):
    if board[0][0] == board[0][1] == board[0][2] == player:
        return True
    for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[0][2] == board[1][1] == board[2][0] == player:
                return True
    return False
running = True
while running:
    print_board()
    print("Player", current_player, "turn")
    row = int(input("Enter row 0, 1, or 2: "))
    col = int(input("Enter column 0, 1, or 2: "))
    if board[row][col] == "-":
        board[row][col] = current_player
    else:
        print("That spot is taken! Try again.")
        continue

    if check_win(current_player):
        print_board()
        print("Player", current_player, "wins!")
        running = False
    if current_player == "X":
        current_player = "O"
    else:
            current_player = "X"
