"""
Iterate through each pixel of the input grid.
Identify all azure (8) pixels.
For each azure pixel, check if there is an adjacent azure pixel to its immediate right.
If there is *no* azure pixel to the immediate right, place a blue (1) pixel in the cell immediately to the right of the current azure pixel.
All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel of the input grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is azure (8)
            if input_grid[r, c] == 8:
                # Check for adjacent azure pixel to the right
                if c + 1 >= cols or input_grid[r, c + 1] != 8:
                    # Add a blue (1) pixel to the right if no azure neighbor
                    if c + 1 < cols:
                        output_grid[r, c + 1] = 1

    return output_grid