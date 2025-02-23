"""
1.  **Identify the center column:** In a square grid, find the central vertical column.
2.  **Preserve all pixels of Colors 0, 4, and 7, in any position.**
3.  **Check for color changes only if there are any changes at all.**
4.  **Specific Changes**:
    *   If there is green (3) in the central column, change it to blue (1)
    *   If there is blue (1) *not* in the center column, change it to green (3)
5.  **All other pixels remain unchanged.**
"""

import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)  # Initialize output grid with the original values
    rows, cols = input_grid.shape
    center_col = cols // 2  # Integer division to find center column.

    # Check if colors 4 or 7 are present. If so, return input grid as is.
    if 4 in input_grid or 7 in input_grid:
        return output_grid

    # Iterate over each cell of input and apply rule
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3 and c == center_col:  # Green and in center column.
                output_grid[r, c] = 1
            elif input_grid[r, c] == 1 and c != center_col:  # Blue and not in center column.
                output_grid[r, c] = 3
    return output_grid