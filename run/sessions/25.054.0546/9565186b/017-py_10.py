"""
Replace all azure (8) pixels in the input grid with gray (5) pixels.
"""

import numpy as np

def transform(input_grid):
    # Create a copy of the input grid to modify.  This ensures we don't change the original.
    output_grid = np.copy(input_grid)

    # Iterate through all pixels in the grid using nested loops.
    for row_index in range(output_grid.shape[0]):
        for col_index in range(output_grid.shape[1]):
            # Check if the current pixel is azure (8).
            if output_grid[row_index, col_index] == 8:
                # Replace azure with gray (5).
                output_grid[row_index, col_index] = 5

    return output_grid