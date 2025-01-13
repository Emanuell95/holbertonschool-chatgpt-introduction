def print_board(board):
    """
    Print the Tic Tac Toe board with rows and columns formatted.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there's a winner in the Tic Tac Toe game.
    Returns True if there's a winner, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Check if the board is full with no empty spaces.
    Returns True if full, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play Tic Tac Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Validate input range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue

            # Check if the chosen spot is empty
            if board[row][col] == " ":
                board[row][col] = player
                # Check for a winner
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                # Check for a draw
                if is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                # Switch players
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

if __name__ == "__main__":
    tic_tac_toe()
