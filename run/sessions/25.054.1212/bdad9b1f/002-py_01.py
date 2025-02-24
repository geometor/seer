"""
1.  **Identify Key Features:** Locate the horizontal row containing red pixels (value '2') and the vertical column containing azure pixels (value '8').

2.  **Intersection:** Find the cell where the identified row and column intersect. Change this cell's value to yellow (value '4').

3.  **Propagation:**  Extend the red pixels (2) to the right along the row until you meet the cell intersecting the azure column.

4.  **Replicate:** Copy the azure pixels vertically along the whole column.
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
    
    # intersection point to yellow
    output_grid[red_row, azure_col] = 4

    # extend red to intersection
    for j in range(input_grid.shape[1]):
        if output_grid[red_row,j] == 0:
            output_grid[red_row,j] = 2
        if j == azure_col:
            break
    
    # fill azure down the column
    for i in range(output_grid.shape[0]):
        output_grid[i, azure_col] = 8
    
    return output_grid