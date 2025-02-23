"""
1.  Find all objects of different colors.
2.  Move object 9 in the last row, preserving its original column
3.  All other objects remain stationary.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all distinct single-cell objects in the grid.
    Returns a dictionary of color: position pairs.
    """
    objects = {}
    for row_idx, row in enumerate(grid):
        for col_idx, color in enumerate(row):
            if color != 0:  # Assuming 0 is the background color
                objects[color] = (row_idx, col_idx)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find objects in the input grid
    objects = find_objects(input_grid)
    
    # Get last row index
    last_row = output_grid.shape[0] - 1

    # Move object 9 to the last row, preserving its column
    if 9 in objects:
        pos_9 = objects[9]
        output_grid[last_row, pos_9[1]] = 9
        if pos_9[0] != last_row:
            output_grid[pos_9[0],pos_9[1]] = 0

    return output_grid