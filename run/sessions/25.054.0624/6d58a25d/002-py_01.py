"""
The transformation rule is as follows:
1. Iterate through each cell of the input grid.
2. Check if the current cell is an azure (8) pixel.
3. If a pixel is azure, then copy that azure pixel to the output grid at the same position.
   Additionally add an azure pixel *above* the current azure pixel (row - 1). If the row above is row 0, do nothing.
4. Locate the cluster of maroon pixels in the grid, and Copy all maroon pixels to the output.
5. Any azure pixels that overlay maroon pixels will replace the maroon.
6. All other pixels (white/0) remain unchanged in their respective positions.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid

    rows, cols = input_grid.shape

    # Iterate over each cell
    for r in range(rows):
        for c in range(cols):
            # Check for azure pixels
            if input_grid[r, c] == 8:
                # Add azure pixel above if not in the first row
                if r > 0:
                    output_grid[r - 1, c] = 8

    return output_grid