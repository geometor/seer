"""
Identifies red (2) pixels in the input grid. Changes isolated red pixels (those not
part of a contiguous horizontal or vertical line of red pixels) to azure (8).
Other pixels remain unchanged.
"""

import numpy as np

def is_part_of_line(grid, row, col, color):
    """
    Checks if a pixel at (row, col) is part of a horizontal or vertical line
    of the specified color.
    """
    rows, cols = grid.shape
    # Check horizontal neighbors
    if (col > 0 and grid[row, col - 1] == color) or \
       (col < cols - 1 and grid[row, col + 1] == color):
        return True
    # Check vertical neighbors
    if (row > 0 and grid[row - 1, col] == color) or \
       (row < rows - 1 and grid[row + 1, col] == color):
        return True
    return False

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel of the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the pixel is red (2)
            if input_grid[row, col] == 2:
                # Check if the red pixel is part of a contiguous line
                if not is_part_of_line(input_grid, row, col, 2):
                    # Change isolated red pixels to azure (8)
                    output_grid[row, col] = 8

    return output_grid