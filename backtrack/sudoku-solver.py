'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
'''

from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        
        def place_num(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
        
        def could_place(d: int, row: int, col: int) -> bool:
            """
            Check whether digit `d` can be placed at `board[row][col]` without violating Sudoku rules:
            - The digit must not already be in the current row, column, or box.
            Returns True if placement is valid; False otherwise.
            """
            # Check row, column, and 3x3 box for existence of digit d
            return not (
                d in rows[row]           # Check if `d` is already used in this row
                or d in cols[col]        # Check if `d` is already used in this column
                or d in boxes[box_index(row, col)]  # Check if `d` is already used in this box
            )

        def remove_num(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_nums(row, col):
            if col == 8 and row == 8:
                nonlocal solved 
                solved = True
            else:
                if col == 8:
                    backtrack(row+1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row = 0, col = 0):
            if board[row][col] == '.':
                for i in range(1, 10):
                    if could_place(i, row, col):
                        place_num(i, row, col)
                        place_next_nums(row, col)
                        if not solved:
                            remove_num(i, row, col)
            else: 
                place_next_nums(row, col)
        
        box_index = lambda row, col: (row // 3) * 3 + col // 3

        rows = [defaultdict(int) for i in range (9)]
        cols = [defaultdict(int) for i in range (9)]
        boxes = [defaultdict(int) for i in range (9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_num(d,i,j)

        solved = False
        backtrack()
        