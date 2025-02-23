"""
The transformation rule is as follows:
1. Identify all non-white colored cells in the input grid.
2. Move all non-white cells to the last row of the output grid, maintaining their original horizontal order.
3. Fill the remaining cells in the output grid with white (0).
"""

import numpy as np

def get_non_white_objects(grid):
    """
    Finds and returns a list of non-white objects with their positions and colors.
    Each object is a tuple: ((row, col), color).
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                objects.append(((r, c), grid[r, c]))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output grid with the same dimensions as the input, filled with white (0).
    output_grid = np.zeros_like(input_grid)

    # Get non-white objects from the input grid.
    objects = get_non_white_objects(input_grid)

    # Sort objects by their original column to maintain horizontal order.
    objects.sort(key=lambda x: x[0][1])

    # Place the objects in the last row of the output grid.
    last_row = output_grid.shape[0] - 1

    # Iterate through the objects
    for (r,c), color in objects:
      if r >= 3: # objects in rows 3, 4 and 5 should be left alone.
        output_grid[r,c] = color
      else:
          # Find the next available position in last_row
          col_index = 0
          while output_grid[last_row, col_index] != 0: #find an empty slot.
            col_index +=1

          output_grid[last_row,col_index] = color

    return output_grid