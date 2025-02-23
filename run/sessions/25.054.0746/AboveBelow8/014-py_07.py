"""
The transformation filters out all colors except azure (8), keeping the azure pixels in their original positions and replacing everything else with white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input, filled with white (0).
    output_grid = np.zeros_like(input_grid)

    # Iterate through the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # If the pixel is azure (8), copy it to the output grid.
            if input_grid[i, j] == 8:
                output_grid[i, j] = 8

    return output_grid