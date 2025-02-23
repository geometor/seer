"""
1. Input: A 3x3 grid where each cell contains a single-digit integer (0-9).
2. Transformation: For each cell in the grid, increment its integer value by 1.
3. Output: A 3x3 grid with the incremented integer values. The layout stays the same.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Increment the value of the cell by 1
            output_grid[i, j] += 1

    return output_grid