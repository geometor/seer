"""
The transformation doubles the width of the input grid, copies the original input to the left half,
and mirrors the orange (7) pattern to the right half. The mirroring is done with respect to the
center of the new, wider grid. The remaining spaces are filled with white (0) pixels.
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

    # Mirror orange pattern to the right side
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 7:
                mirrored_j = cols * 2 - 1 - j  # Calculate mirrored column index
                output_grid[i, mirrored_j] = 7

    return output_grid