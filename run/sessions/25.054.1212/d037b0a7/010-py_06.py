"""
If a pixel is white (0), and the pixel directly *above* it has a different, non-zero color, then set the current pixel's color to the color of the pixel above it.
After applying the above rule to all cells, examine each pixel in the grid, row by row, and left to right.
If a pixel is not white, and the pixel to it's right is a `0` (white), set all `0` pixels to it's right to match the pixel's color until you encounter a non-white pixel.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell of the grid, applying the downward propagation rule.
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 0:  # If the current pixel is white
                if i > 0:  # Check if there's a row above
                    if output_grid[i - 1, j] != 0:  # If the pixel above is not white
                        output_grid[i, j] = output_grid[i - 1, j]  # Set color to the pixel above

    # Iterate through the grid again to apply fill to the right rule
    for i in range(rows):
        for j in range(cols):
            if output_grid[i,j] != 0:
                for k in range(j+1, cols):
                    if output_grid[i,k] == 0:
                        output_grid[i,k] = output_grid[i,j]
                    else:
                        break # stop when a non-white is encountered

    return output_grid