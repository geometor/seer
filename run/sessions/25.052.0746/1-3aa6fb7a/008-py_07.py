"""
The transformation rule can be described as follows:

1.  **Identify "L" shapes:** Locate all "L" shaped objects within the grid. These "L" shapes are composed of three adjacent cells of color 8 (azure) forming a 2x2 block with one cell missing. There are four possible orientations for the "L" shape (normal, mirrored, and rotated).

2.  **Check Orientation and Position:** For each identified "L" shape:

    *   If it's a "right-facing" L (the single cell is on the right), and the cell to the *right* of the corner of the "L" is within the grid bounds, change the color of that adjacent cell to 1 (blue). The 'corner' is the single 8 in that configuration.
    *    If it is a "left-facing" L (the single cell is on the left), and the cell immediately to the *left* of the corner of the "L" is within bounds, change that adjacent cell's color to 1 (blue). The 'corner' is the single 8.

3. **No other changes:** All other cells in the grid retain their original colors.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on identifying 'L' shaped objects of color 8 and changing adjacent cells to color 1.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        for c in range(cols):
            # Check for right-facing L
            if (r > 0 and c < cols - 1 and
                output_grid[r, c] == 8 and
                output_grid[r - 1, c] == 8 and
                output_grid[r - 1, c + 1] == 8):
                output_grid[r, c + 1] = 1

            # Check for left-facing L
            if (r < rows - 1 and c > 0 and
                output_grid[r, c] == 8 and
                output_grid[r, c - 1] == 8 and
                output_grid[r + 1, c - 1] == 8):
                output_grid[r, c - 1] = 1

            # Check for bottom-left-facing L
            if (r > 0 and c > 0 and
                output_grid[r, c] == 8 and
                output_grid[r, c - 1] == 8 and
                output_grid[r - 1, c - 1] == 8):
                    output_grid[r, c-1] = 1

            # Check for top-right-facing L
            if (r < rows -1 and c < cols - 1 and
                output_grid[r,c] == 8 and
                output_grid[r, c+1] == 8 and
                output_grid[r+1,c+1] == 8):
                    output_grid[r,c+1] = 1
    return output_grid