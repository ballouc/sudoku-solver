# TODO
'''
1. Implement basic Sudoku game rules with static puzzle
2. Wave Function Collapse algorithmic solver using cells' superpositions
3. Utilize Python GUI library to create visual representation of Sudoku game
4. QoL features (notes, cleared nums, puzzle generation, visual solving)
'''

# 0 represents a blank space
sudoku_grid = [
            [0,0,8,0,0,0,0,1,6],
            [5,0,0,0,9,2,0,0,8],
            [0,0,0,1,0,0,0,0,0],
            [9,0,0,3,0,0,8,2,0],
            [0,2,0,0,0,0,0,7,0],
            [0,8,4,0,0,6,0,0,5],
            [0,0,0,0,0,3,0,0,0],
            [4,0,0,9,6,0,0,0,2],
            [1,6,0,0,0,0,7,0,0]
          ]

def is_valid(row_number, column_number, number):
    global sudoku_grid

    for n in range(0,9):
        if sudoku_grid[row_number][n] == number:
            return False
    for n in range(0,9):
        if sudoku_grid[n][column_number] == number:
            return False
        
    square_row = row_number // 3 * 3
    square_col = column_number // 3 * 3
    for n in range(0,3):
        for m in range(0,3):
            if sudoku_grid[square_row + n][square_col + m] == number:
                return False
            
    return True
        
    