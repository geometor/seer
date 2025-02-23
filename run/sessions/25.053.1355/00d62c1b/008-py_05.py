"""
1.  **Identify Connected Components:** Find all groups of green (3) pixels that are connected to each other. Two green pixels are connected if you can move between them by going up, down, left, or right without encountering a non-green pixel. Each of these groups is a "connected component."

2.  **Define Interior Pixels:** A green pixel within a connected component is considered "interior" if it meets *all* of the following conditions:
    *   It has a green neighbor above it.
    *   It has a green neighbor below it.
    *   It has a green neighbor to its left.
    *   It has a green neighbor to its right.

3.  **Transform Interior Pixels:** Change the color of all identified "interior" green pixels to yellow (4).

4.  **Leave Other Pixels Unchanged:** All other pixels that are not "interior" green pixels within a connected component remain their original color.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    def is_interior(i, j):
        """Checks if a green pixel is interior to a connected component."""
        if input_grid[i, j] != 3:
            return False

        up = i > 0 and input_grid[i-1, j] == 3
        down = i < rows - 1 and input_grid[i+1, j] == 3
        left = j > 0 and input_grid[i, j-1] == 3
        right = j < cols - 1 and input_grid[i, j+1] == 3

        return up and down and left and right # All four neighbors must be green

    # Iterate through each cell of the grid.
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is an interior green pixel.
            if is_interior(i, j):
                # Change the color of the current cell to yellow (4).
                output_grid[i, j] = 4

    return output_grid