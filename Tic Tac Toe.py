def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winning combination
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while True:
        player = players[turn % 2]
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = player
        display_board(board)

        if check_winner(board, player):
            print(f"Congratulations! Player {player} wins!")
            break

        if turn == 8:
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()