"""
1.  **Find Red Row:** Find the index of the row that contains at least one red pixel.
2.  **Find Azure Column:** Find the index of the column that contains at least one azure pixel.
3.  **Mark Intersection:** Change the color of the cell at the intersection of the red row and azure column to yellow.
4.  **Extend Red:**  In the red row, change the color of all pixels to red, starting from the first column (index 0) up to *and including* the azure column's index.
5.  **Extend Azure:**
    *   Check for azure pixels *above* the red row within the azure column. If found, change all cells in the azure column *above* the red row to azure.
    *   Check for azure pixels *below* the red row within the azure column. If found, change all cells in the azure column *below* the red row to azure.
"""

import numpy as np

def find_row_with_color(grid, color):
    for i, row in enumerate(grid):
        if color in row:
            return i
    return -1

def find_col_with_color(grid, color):
    grid_t = grid.transpose()
    for i, col in enumerate(grid_t):
        if color in col:
            return i
    return -1

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find the red row and azure column
    red_row = find_row_with_color(input_grid, 2)
    azure_col = find_col_with_color(input_grid, 8)

    if red_row == -1 or azure_col == -1:
        return output_grid
    
    # extend red to intersection (inclusive)
    for j in range(azure_col + 1):
        output_grid[red_row,j] = 2

    # intersection point to yellow
    output_grid[red_row, azure_col] = 4
    
    # fill azure down the column conditionally
    azure_above = False
    azure_below = False

    for i in range(red_row):
        if input_grid[i, azure_col] == 8:
            azure_above = True
            break

    for i in range(red_row + 1, input_grid.shape[0]):
        if input_grid[i, azure_col] == 8:
            azure_below = True
            break

    if azure_above:
      for i in range(red_row):
          output_grid[i, azure_col] = 8
    if azure_below:
      for i in range(red_row+1, output_grid.shape[0]):
          output_grid[i, azure_col] = 8

    
    return output_grid