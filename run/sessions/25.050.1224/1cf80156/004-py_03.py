"""
Locate the contiguous object of color 9. 
Determine the smallest rectangle (bounding box) that encompasses it.
Reflect the subgrid defined by the bounding box along both vertical and horizontal axes.
"""

import numpy as np

def get_bounding_box(grid, color):
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find the bounding box of the object with color 9.
    bounding_box = get_bounding_box(input_grid, 9)
    if bounding_box is None:
        return np.zeros_like(input_grid)  # Return an empty grid if no object of color 9

    (min_row, min_col), (max_row, max_col) = bounding_box

    # Extract the subgrid within the bounding box.
    subgrid = input_grid[min_row:max_row+1, min_col:max_col+1]

    # Reflect the subgrid horizontally and vertically.
    reflected_subgrid = np.flip(subgrid)

    return reflected_subgrid