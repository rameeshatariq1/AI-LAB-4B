# N-Queens Problem (Dynamic)

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i in range(row):
        if board[i] - i == col - row:
            return False

    # Check right diagonal
    for i in range(row):
        if board[i] + i == col + row:
            return False

    return True


def solve_n_queens(n):
    board = [-1] * n  # board[i] = column position of queen in row i

    def solve(row):
        if row == n:
            print_solution(board, n)
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                if solve(row + 1):
                    return True
                board[row] = -1  # Backtracking

        return False

    if not solve(0):
        print("No solution exists")


def print_solution(board, n):
    print("\n Solution Found:\n")
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Take dynamic input
n = int(input("Enter value of N: "))
solve_n_queens(n)