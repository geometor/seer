"""
The transformation rule is as follows:
1. Identify the objects of color 9 and 8.
2. Move the object of color 9 to the last row of the grid, maintaining its column position.
3. Move the object of color 8 that is most on top to the last row preserving its column.
4. All other cells in the grid remain the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape
    
    #Move the object of color 9.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 9:
                output_grid[rows - 1, c] = 9
                if r!= rows-1:
                    output_grid[r,c] = 0

    # Move one object of color 8
    found = False
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8 and not found:
                output_grid[rows - 1, c] = 8
                if r != rows -1:
                    output_grid[r,c] = 0
                found = True

    return output_grid