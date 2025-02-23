"""
Identifies a contiguous shape of non-white pixels and applies an alternating color fill of azure (8) and red (2),
starting from the top-left pixel of the shape. The background (white - 0) remains unchanged.
"""

import numpy as np

def find_shape(grid):
    # Find the non-white pixels
    rows, cols = np.where(grid != 0)
    
    if len(rows) == 0:  # Handle the case where there are no non-white pixels
        return None, None, None

    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    # Extract the shape as a subgrid
    shape = grid[min_row:max_row+1, min_col:max_col+1]
    
    return shape, (min_row, min_col), (max_row, max_col)


def transform(input_grid):
    """
    Transforms the input grid by applying an alternating color fill to the identified shape.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the shape and its bounding box
    shape, top_left, _ = find_shape(input_grid)

    if shape is None:  # No shape found, return the original grid
        return output_grid

    start_row, start_col = top_left

    # Iterate through the bounding box and apply the alternating fill
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            if shape[i,j] != 0:
               if (i + j) % 2 == 0:
                   output_grid[start_row + i, start_col + j] = 8  # Azure
               else:
                   output_grid[start_row + i, start_col + j] = 2  # Red

    return output_grid