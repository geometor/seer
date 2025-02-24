"""
Finds all blue (1) pixels. For each blue pixel, changes it to red (2).
Then, propagates the red color upwards, changing any white (0) pixels to red (2)
until a non-white pixel or the top edge of the grid is reached.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Get the dimensions of the grid.
    rows, cols = output_grid.shape

    # Iterate through each cell of the input grid to find blue pixels.
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 1:  # Found a blue pixel
                # Change the blue pixel to red.
                output_grid[r, c] = 2
                # Propagate the red color upwards.
                current_row = r - 1  # Start at the row above
                while current_row >= 0 and output_grid[current_row, c] == 0:
                    output_grid[current_row, c] = 2  # Change white to red
                    current_row -= 1  # Move to the next row above

    return output_grid