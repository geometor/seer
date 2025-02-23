"""
The input grid is transformed into the output grid by replacing, in each row, groups of three horizontal cells with the sequence '1 0 3' (blue, white, green), repeating this pattern across the entire row.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each row
    for i in range(rows):
        # Apply the sequence '1 0 3' repeatedly across the row
        for j in range(0, cols, 3):
            output_grid[i, j:min(j+3, cols)] = [1, 0, 3][:min(3, cols-j)] # Handle edge case, if any

    return output_grid