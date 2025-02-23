"""
The transformation identifies an outer red rectangle and an inner green rectangle. 
The central vertical column of the inner rectangle is modified.
Green pixels are added ("creep") vertically from the center of the original green rectangle,
stopping when encountering a different color.
"""

import numpy as np

def find_object(grid, color):
    """Finds the bounding box of an object with a specific color."""
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return (min_row, min_col), (max_row, max_col)

def get_central_column(top_left, bottom_right):
    """Calculates the central column index."""
    _, min_col = top_left
    _, max_col = bottom_right
    central_col = (min_col + max_col) // 2
    return central_col

def creeping(grid, start_row, start_col, color):
    """Adds pixels of a given color vertically from a starting point until non-matching color."""
    rows, cols = grid.shape
    # Creep upwards
    row = start_row -1
    while row >= 0:
        if grid[row,start_col] != 2:
           break;

        grid[row, start_col] = color
        row -= 1

    row = start_row + 1
    while row < rows:
        if grid[row,start_col] != 2:
           break;

        grid[row, start_col] = color
        row += 1

    return grid
    

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the outer red rectangle
    outer_top_left, outer_bottom_right = find_object(input_grid, 2)

    # Find the inner green rectangle
    inner_top_left, inner_bottom_right = find_object(input_grid, 3)
   
    if inner_top_left is None or outer_top_left is None:
       return output_grid

    # Get the central column of the green rectangle
    central_col = get_central_column(inner_top_left, inner_bottom_right)
    inner_min_row, _ = inner_top_left
    inner_max_row, _ = inner_bottom_right

    # modify the inner object
    for row in range(inner_min_row, inner_max_row + 1):
        output_grid[row, central_col] = 2

    center_row = (inner_top_left[0] + inner_bottom_right[0]) // 2
    
    output_grid = creeping(output_grid, center_row, central_col, 3)

    return output_grid