"""
Transforms the top half of the input grid to a 3x3 output grid, mapping maroon (9) to red (2) and keeping white (0) as white (0), preserving relative positions within the top half.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 3x3 output grid filled with zeros.
    output_grid = np.zeros((3, 3), dtype=int)
    input_height = input_grid.shape[0]
    input_width = input_grid.shape[1]

    # Consider only the top half of the input grid.
    for i in range(min(3, input_height // 2 )): # Iterate through top half, up to 3 rows.
        for j in range(min(3,input_width)):  #Iterate through the columns
            # Map colors and positions.
            if input_grid[i][j] == 9:
                output_grid[i][j] = 2
            elif input_grid[i][j] == 0:
                output_grid[i][j] = 0

    return output_grid