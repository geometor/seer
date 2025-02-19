"""
Isolate the azure object and find the bounding box.
The bounding box defines the output grid.
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
    """
    Transforms the input grid by extracting the bounding box
    around the azure object.
    """
    input_grid = np.array(input_grid)

    # Find the bounding box of the azure object (color 8).
    bounding_box = get_bounding_box(input_grid, 8)
    if bounding_box is None:
        return np.zeros((3, 5), dtype=int)  # Return an empty output grid

    (min_row, min_col), (max_row, max_col) = bounding_box

    # Extract the subgrid within the bounding box.
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid