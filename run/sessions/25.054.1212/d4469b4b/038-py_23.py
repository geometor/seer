"""
Identifies contiguous blocks of green (3) pixels in the input grid,
creates a smaller grid representing the "shape" of the object formed by those contiguous blocks,
and recolors the green blocks to gray, maintaining white pixels as white.
"""

import numpy as np

def get_object_indices(grid, color):
    """
    find the indices of an object in a grid given its color
    """
    return np.argwhere(grid == color)

def transform(input_grid):
    """
    Transforms the input grid according to the described rules.
    """
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # 1. Identify Contiguous Blocks (green pixels)
    green_indices = get_object_indices(input_grid, 3)

    # 2. Determine output dimension
    if len(green_indices) > 0:
       rows = np.unique(green_indices[:, 0])
       cols = np.unique(green_indices[:, 1])
       output_height = len(rows)
       output_width = len(cols)
    else:
       output_height = 0
       output_width = 0

    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Find min_row, min_col to "normalize" position within new grid
    if (output_height > 0) and (output_width > 0):
        min_row = np.min(rows)
        min_col = np.min(cols)

        # 3. Recolor and place in the output grid
        for i,j in green_indices:
            output_grid[i-min_row, j-min_col] = 5

    return output_grid.tolist()