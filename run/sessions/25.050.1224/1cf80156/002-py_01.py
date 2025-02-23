"""
Isolate the red object, find the bounding box,
and create a 4x4 checkerboard pattern filling the
positions where the original object pixels where.
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
    Transforms the input grid by isolating the red object,
    creating a bounding box, and generating a checkerboard pattern.
    """
    input_grid = np.array(input_grid)

    # Identify the red object (color 2).
    red_pixels = (input_grid == 2)

    # Find the bounding box.
    (min_row, min_col), (max_row, max_col) = get_bounding_box(input_grid, 2)
    
    # Initialize the output grid (4x4).
    output_grid = np.zeros((4, 4), dtype=int)
    
    # create mapping from the original shape coordinates
    # to the output grid coordinates

    for i in range(4):
        for j in range(4):
            orig_row = min_row + int( (i/4) * (max_row - min_row +1))
            orig_col = min_col + int( (j/4) * (max_col- min_col +1))
            if input_grid[orig_row,orig_col]==2:
                output_grid[i,j] = 2
            elif (i+j) % 2 == 0:
                 output_grid[i,j] = 0
            else:
                 output_grid[i,j] = 2
    return output_grid