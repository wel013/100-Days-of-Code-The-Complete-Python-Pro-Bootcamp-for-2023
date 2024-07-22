# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
board = [[" " for _ in range(3)] for _ in range(3)]


def check_rows(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    return False


def check_cols(board):
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    return False


def check_diagonals(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    # Anti-diagonal
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False


def check_end_of_game(board):
    return check_cols(board) or check_rows(board) or check_diagonals(board)


end_game = False


for i in range(9):
    if i % 2 == 0:
        step = input(
            "You are O, please select where you want to place in row, col format ")
        symbol = "O"
    elif i % 2 != 0:
        step = input(
            "You are X, please select where you want to place in row, col format ")
        symbol = "X"

    row = int(step[0])-1
    col = int(step[2])-1
    if board[row][col] != " ":
        step = input("You cannot place it there, please re-enter")
        row = int(step[0])-1
        col = int(step[2])-1
    try:
        board[row][col] = symbol
    except IndexError:
        print("You cannot put it here")
        step = input(
            "Re-enter please ")
        row = int(step[0])-1
        col = int(step[2])-1
        board[row][col] = symbol

    for i in range(3):
        for j in range(3):
            if j < 2:  # Print the separator after every row except the last one
                print(board[i][j], end=" | ")
            else:
                print(board[i][j], end='')
        print()  # Move to the next line after printing each row
        if i < 2:  # Print the separator after every row except the last one
            print("----------")
    end_game = check_end_of_game(board)
    # print(end_game)

    if end_game:
        print("You won!")
        break
if not end_game:
    print("It is a tie!")
