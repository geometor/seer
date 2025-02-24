"""
Iterates through each pixel of the input grid and performs a color swap:
- If the pixel is blue (1), change it to gray (5) in the output grid.
- If the pixel is gray (5), change it to blue (1) in the output grid.
- If the pixel is white (0), keep it as white (0) in the output grid.
Maintains the original grid structure and dimensions.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    # Get the dimensions of the grid
    rows, cols = output_grid.shape

    # Iterate through each pixel of the grid
    for i in range(rows):
        for j in range(cols):
            # Check the color of the current pixel
            if input_grid[i, j] == 1:  # If blue
                output_grid[i, j] = 5  # Change to gray
            elif input_grid[i, j] == 5:  # If gray
                output_grid[i, j] = 1  # Change to blue
            # White (0) remains unchanged

    return output_grid