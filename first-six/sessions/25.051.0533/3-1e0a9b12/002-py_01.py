"""
1. Find all objects of different colors.
2. Move objects in the last row, preserving its horizontal order.
3. Move one object '4' one row up.
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
    output_grid[:] = 0

    # Find objects in the input grid
    objects = find_objects(input_grid)
    
    # Get last row index
    last_row = output_grid.shape[0] - 1

    # Sort objects by their column index to preserve horizontal order
    sorted_objects = sorted(objects.items(), key=lambda item: item[1][1])

    # Move objects to the last row, preserving horizontal order
    for color, pos in sorted_objects:
        output_grid[last_row, pos[1]] = color
    
    #Find position of object with color 4
    pos_4 = [pos for color, pos in objects.items() if color == 4 ]
    
    #Move one color 4 one position up, if present
    for pos in pos_4:
      if output_grid[last_row,pos[1]] == 4:
        output_grid[last_row - 1, pos[1]] = 4
        output_grid[last_row,pos[1]] = 0

    return output_grid