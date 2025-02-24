"""
Transforms an input grid based on the following rules:

1. Check the entire grid for the presence of green (3) in the bottom row.
2. Iterate through each pixel:
   - If the pixel is not green (3), it remains unchanged.
   - If the pixel is green (3):
     - If the pixel is in the top two rows (row index 0 or 1) AND there are NO green pixels in the bottom row, change it to azure (8).
     - Otherwise (pixel is in the bottom row, OR there ARE green pixels in the bottom row), leave it unchanged.
"""

import numpy as np

def _has_green_in_bottom_row(grid):
    """Checks if the bottom row of a grid contains any green (3) pixels."""
    rows, cols = grid.shape
    return 3 in grid[rows - 1, :]

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Check for green in the bottom row (global condition).
    bottom_row_green = _has_green_in_bottom_row(output_grid)

    # Iterate through the grid and apply the transformation rules.
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 3:  # Check if the cell is green.
                if r < 2 and not bottom_row_green:  # Top two rows AND no green in bottom row.
                    output_grid[r, c] = 8  # Change to azure.
                # Else: Leave green pixel unchanged (already in output_grid).
            # Non-green pixels are also implicitly unchanged.

    return output_grid