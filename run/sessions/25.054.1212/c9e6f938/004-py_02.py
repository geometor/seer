"""
The transformation doubles the width of the input grid, copies the original input to the left half,
and duplicates the orange (7) pattern to the right half, adjacent to the original pattern.
The remaining spaces are filled with white (0) pixels.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid by doubling the width of the input grid.
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols * 2), dtype=int)

    # Copy the original input to the left side of the output grid.
    for i in range(rows):
        output_grid[i, :cols] = input_grid[i]

    # Duplicate orange pattern to adjacent columns
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 7:
                output_grid[i, j + cols] = 7

    return output_grid