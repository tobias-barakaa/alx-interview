#!/usr/bin/python3
"""
N queens problem
"""

import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    """
    Utility function to solve N Queens problem using backtracking
    """
    if col == n:
        # If all queens are placed, print the solution
        solution = [[row, board[row].index(1)] for row in range(n)]
        print(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen and recursively solve for the next column
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n)
            # Backtrack and undo the queen placement if the solution is not found
            board[i][col] = 0

def solve_nqueens(n):
    """
    Main function to solve the N Queens problem
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Start solving from the first column
    solve_nqueens_util(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])

