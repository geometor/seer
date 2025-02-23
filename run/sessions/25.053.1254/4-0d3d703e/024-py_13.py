"""
Transforms a 3x3 grid based on a conditional color mapping. The mapping applied to the first two columns
depends on the value in the last column. The last column itself also undergoes specific changes.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through rows
    for i in range(rows):
        # Apply mapping to the first two columns based on last column's value
        last_col_val = input_grid[i, cols - 1]

        for j in range(cols - 1):  # Iterate through the first two columns only
            if last_col_val == 2:
                if input_grid[i, j] == 3:
                    output_grid[i, j] = 4
                elif input_grid[i, j] == 1:
                    output_grid[i, j] = 5
                elif input_grid[i, j] == 5:
                    output_grid[i, j] = 1
                elif input_grid[i, j] == 8:
                    output_grid[i,j] = 8

            elif last_col_val == 8:
                if input_grid[i, j] == 2:
                    output_grid[i, j] = 6
                elif input_grid[i, j] == 3:
                    output_grid[i, j] = 4
        #change last column values
        if last_col_val == 2:
            output_grid[i,cols-1] = 6
        elif last_col_val == 8:
            output_grid[i,cols-1] = 9

    return output_grid