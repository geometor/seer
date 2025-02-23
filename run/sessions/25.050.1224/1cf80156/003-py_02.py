"""
Isolate the blue object, create its bounding box,
and map the pixels to the output grid.
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
    around the blue object and remapping to the output grid.
    """
    input_grid = np.array(input_grid)

    # Find the bounding box of the blue object (color 1).
    bounding_box = get_bounding_box(input_grid, 1)
    if bounding_box is None:
        return np.zeros((5, 3), dtype=int)  # Return an empty output grid if no blue object

    (min_row, min_col), (max_row, max_col) = bounding_box

    # Initialize an output grid of the appropriate.
    output_grid = np.zeros((5, 3), dtype=int)

    # create mapping from the original shape coordinates
    # to the output grid coordinates

    for i in range(5):
        for j in range(3):
            orig_row = min_row + int( (i/5) * (max_row - min_row +1))
            orig_col = min_col + int( (j/3) * (max_col- min_col +1))
            if input_grid[orig_row,orig_col]==1:
                output_grid[i,j] = 1
            
    return output_grid