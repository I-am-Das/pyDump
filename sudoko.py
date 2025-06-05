def print_board(board):
    print("\n-------------------------")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("-------------------------")

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def is_valid(board, num, pos):
    row, col = pos

    for c in range(9):
        if board[row][c] == num and col != c:
            return False

    for r in range(9):
        if board[r][col] == num and row != r:
            return False

    box_x = col // 3
    box_y = row // 3

    for r_in_box in range(box_y * 3, box_y * 3 + 3):
        for c_in_box in range(box_x * 3, box_x * 3 + 3):
            if board[r_in_box][c_in_box] == num and (r_in_box, c_in_box) != pos:
                return False
    return True

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True

    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def main():
    initial_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    game_board = [row[:] for row in initial_board]
    fixed_cells = [(r, c) for r in range(9) for c in range(9) if initial_board[r][c] != 0]

    print("Welcome to Simple Sudoku!")
    print("Fill in the empty cells (represented by 0).")
    print("Enter 'q' to quit.")

    while True:
        print_board(game_board)

        if not find_empty(game_board) and is_valid_board_complete(game_board):
            print("\n********** CONGRATULATIONS! You solved the Sudoku! **********")
            break
        elif not find_empty(game_board) and not is_valid_board_complete(game_board):
            print("\nBoard is full, but there are still errors. Keep trying!")

        try:
            user_input = input("Enter your move (row col num, e.g., '1 2 5') or 'q' to quit: ").strip().lower()

            if user_input == 'q':
                print("Quitting game. Goodbye!")
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input format. Please use 'row col num'.")
                continue

            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
            num = int(parts[2])

            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                print("Invalid row, column (1-9) or number (1-9). Please try again.")
                continue

            if (row, col) in fixed_cells:
                print("You cannot change an original puzzle number!")
                continue

            if is_valid(game_board, num, (row, col)):
                game_board[row][col] = num
                print("Move accepted.")
            else:
                print("Invalid move! This number is already in the row, column, or 3x3 box.")

        except ValueError:
            print("Invalid input. Please enter numbers for row, column, and value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def is_valid_board_complete(board):
    temp_board = [row[:] for row in board]
    return solve_sudoku(temp_board)

if __name__ == "__main__":
    main()
