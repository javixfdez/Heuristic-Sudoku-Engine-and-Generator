
import random as rn
 
class Sudoku:
    def __init__(self, board=None):
        #We initialize our board of the sudoku
        self.board = self.board = board if board else [[0 for _ in range(9)] for _ in range(9)]
 
    def print_sudoku(self):
        if self.find_empty():
            print("\nOriginal Sudoku\n")
        else:
            print("\nSolved Sudoku\n")
 
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
 
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
 
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
 
    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
 
        return False
   
   
    def valid(self, num, pos):
        #Checks the numbers of the row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False
 
        #Check the numbers of the column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
 
        #Check the sub-box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
 
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False
 
        return True
   
 
    def backtracking_solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
 
        for i in range(1, 10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i
 
                if self.backtracking_solve():
                    return True
 
                self.board[row][col] = 0
 
        return False
   
    def get_possible_numbers_greedy(self, row, col):
        row_counts = [0] * 10
        col_counts = [0] * 10
        box_counts = [0] * 10
 
        # Count occurrences of numbers in the row
        for i in range(9):
            if self.board[row][i] != 0:
                row_counts[self.board[row][i]] += 1
 
        # Count occurrences of numbers in the column
        for i in range(9):
            if self.board[i][col] != 0:
                col_counts[self.board[i][col]] += 1
 
        # Count occurrences of numbers in the 3x3 box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] != 0:
                    box_counts[self.board[i][j]] += 1
 
        # Create a list of possible numbers sorted by their total count in row, column, and box
        possible_numbers = [num for num in range(1, 10) if row_counts[num] == 0 and col_counts[num] == 0 and box_counts[num] == 0]
        possible_numbers.sort(key=lambda x: row_counts[x] + col_counts[x] + box_counts[x])
 
        return possible_numbers
   
    def solve_greedy(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
 
        possible_numbers = self.get_possible_numbers_greedy(row, col)
 
        for num in possible_numbers:
            if self.valid(num, (row, col)):
                self.board[row][col] = num
 
                if self.solve_greedy():
                    return True
 
                self.board[row][col] = 0
 
        return False
   
    def generate_complete_board(self):
        # Start with an empty board
        self.board = [[0 for _ in range(9)] for _ in range(9)]
       
        # Fill the diagonal 3x3 boxes
        for i in range(0, 9, 3):
            self.fill_diagonal_box(i, i)
 
        # Fill the remaining cells
        self.backtracking_solve()
 
    def fill_diagonal_box(self, row, col):
        num_list = list(range(1, 10))
        rn.shuffle(num_list)
        for i in range(3):
            for j in range(3):
                self.board[row + i][col + j] = num_list.pop()
 
    def generate_sudoku(self, num_to_remove=50):
        self.generate_complete_board()
        for _ in range(num_to_remove):
            row, col = rn.randint(0, 8), rn.randint(0, 8)
            while self.board[row][col] == 0:
                row, col = rn.randint(0, 8), rn.randint(0, 8)
            self.board[row][col] = 0
 
board = [
    [1,0,0,0,0,0,0,2,0],
    [0,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,0,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,0,0,0,0,7,0,0,0],
    [0,4,9,2,0,6,0,0,7]
]
 
sudoku=Sudoku()
sudoku.print_sudoku
sudoku.generate_sudoku()
sudoku.print_sudoku
sudoku.backtracking_solve()
sudoku.print_sudoku
 
sudoku2=Sudoku()
sudoku2.generate_sudoku()
sudoku2.print_sudoku
sudoku2.solve_greedy()
sudoku2.print_sudoku

sudoku3=Sudoku()
sudoku3.generate_sudoku()
sudoku3.print_sudoku()
sudoku3.backtracking_solve()
sudoku3.print_sudoku()