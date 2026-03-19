import random as rn
from  SudokuSolver import Sudoku
#We generate different Sudoku boards
boards = [
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ],
        [
            [1, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 0, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ],
        [[0 for _ in range(9)] for _ in range(9)],  # Empty board
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 5, 0, 1, 9, 5, 0, 0, 0],  # Invalid due to repeated '5'
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    ]

for i, board in enumerate(boards):
        print(f"\nBoard {i + 1}:")
        sudoku = Sudoku(board)

        # Print original board
        sudoku.print_sudoku()

        # Solve with backtracking
        print("\nSolving with Backtracking:")
        if sudoku.backtracking_solve():
            sudoku.print_sudoku()
        else:
            print("No solution found with backtracking.")

        # Reset the board to the original state for greedy solve
        sudoku = Sudoku(board)

        # Solve with greedy
        print("\nSolving with Greedy:")
        if sudoku.solve_greedy():
            sudoku.print_sudoku()
        else:
            print("No solution found with greedy.")
