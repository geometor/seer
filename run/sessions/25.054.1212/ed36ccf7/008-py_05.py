"""
Identify Colors: Recognize the two colors present in the input grid: white (0) and magenta (6).

Rotate Magenta: Exchange the positions of colors in first row, copy value at (0,1) to (0,0) and value at (0,2) to (1,2).
    Exchange column value, copy value at (1,0) to (2,0).
    Copy (2,1) to (2,2).

Result: The output grid is the result of the steps applied on the input.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Rotate Magenta:
    # Exchange the positions of colors in the first row
    output_grid[0, 0] = input_grid[0, 1]
    output_grid[1, 2] = input_grid[0, 2]

    # Exchange column value, copy value at (1,0) to (2,0)
    output_grid[2, 0] = input_grid[1, 0]
    
    # Copy (2,1) to (2,2)
    output_grid[2, 2] = input_grid[2, 1]


    return output_grid