"""
Sudoku is a game played on a 9x9 grid. 
The goal of the game is to fill all cells of the grid with digits from 1 to 9, 
so that each column, each row, and each of the nine 3x3 sub-grids 
(also known as blocks) contain all of the digits from 1 to 9.

Write a function that accepts a 2D array representing a Sudoku board, 
and returns true if it is a valid solution, or false otherwise. 

The cells of the sudoku board may also contain 0's, which will represent empty cells. 
Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
"""


def valid_solution(board):
    validator = list(range(1, 10))

    for i in range(len(board)):
            # cols                              # rows
        if sorted([row[i] for row in board]) != sorted(board[i]) != validator:
            return False
        # blocks
        # _valid_solution(board[len(board) % 9: (len(board) % 9) + 3])
        a, b = 0, 3
        while b < 10:
            holding = []
            for row in board[a:b]:
                holding.extend([c for c in row[a:b]])
            if sorted(holding) != validator:
                return False
            a += 3
            b += 3

    return True

# techniques for transposing

# list(zip(*{2d array})) -> returns a transformed 2d array

# for i range(len({2d array}));
#   [row[i] for i in {2d array}] -> returns each column

assert valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True

assert valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                        [6, 7, 2, 1, 9, 0, 3, 4, 9],
                        [1, 0, 0, 3, 4, 2, 5, 6, 0],
                        [8, 5, 9, 7, 6, 1, 0, 2, 0],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 0, 1, 5, 3, 7, 2, 1, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 0, 0, 4, 8, 1, 1, 7, 9]]) == False

# --------------------------------- #
# alternative approaches i liked

# functions
def validSolution(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows

def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not check_one_to_nine(nums):
                return False
    return True

def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True
    
def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True
            

def check_one_to_nine(lst):
    check = range(1,10)
    return sorted(lst) == check


# lambda and iteration
def validSolution(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)    


# nice logic
def valid_solution(m):
    is_valid = lambda a: len(a) == 9 and all([i + 1 in a for i in range(9)])
    get_block_as_row = lambda n: [m[3 * (n / 3) + (i / 3)][(3 * n) % 9 + i % 3] for i in range(9)]
    return all([is_valid(r) for r in m]) and all([is_valid([r[i] for r in m]) for i in range(9)]) and all([is_valid(get_block_as_row(i)) for i in range(9)])
  

# TODO review, what product does
from itertools import product

def validSolution(board):
    rows = board
    columns = map(list, zip(*board))
    blocks = [[board[i][j] for (i, j) in product(xrange(x, x+3), xrange(y, y+3))] for (x, y) in product((0, 3, 6), repeat=2)]
    
    return all(sorted(line) == range(1, 10) for lines in (rows, columns, blocks) for line in lines)
