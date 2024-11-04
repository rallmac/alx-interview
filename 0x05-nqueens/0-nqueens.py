#!/usr/bin/python3
"""This program solves the nqueens puzzle"""

import sys


def print_solution(board):
    """This function prints the solution in the required
       format
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col, N):
    """This function checks if a queen can be placed at board
       [row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if i < N and board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N):
    """Utilizes backtracking to solve the Nqueens problem
    """
    if col >= N:
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N)
            board[i][col] = 0  # backtrack


def nqueens(N):
    """Initialize the board and start solving the puzzle
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must ba a number.")
        sys.exit(1)

    if N < 4:
        print ("N must be at least 4")
        sys.exit(1)

    nqueens(N)
