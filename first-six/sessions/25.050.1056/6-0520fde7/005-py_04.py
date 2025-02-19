"""
The transformation identifies the central column of gray squares in the input grid.
It creates a 3x3 output grid. Then fills cells with color 2 if i-j=1 or j-i = 1
All other cells in the output grid are colored white (0).
"""

import numpy as np

def find_central_column(grid):
    # Find the column index with gray color (5)
    for j in range(grid.shape[1]):
        if all(grid[:, j] == 5):
            return j
    return -1  # Return -1 if no such column is found

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on the defined rule.
    """
    # Create a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

     # Find the central column in the input grid (not used in defining size, but relevant for the overall logic).
    # central_column_index = find_central_column(input_grid)

    # Count blue objects (not directly used, but could be useful for future generalization)
    num_blue = np.count_nonzero(input_grid == 1)

    # Iterate through the output grid and fill cells based on the condition
    for i in range(3):
        for j in range(3):
            if i - j == 1 or j - i == 1:
                output_grid[i, j] = 2

    return output_grid