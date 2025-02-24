"""
1.  **Locate Red Pixels:** Find all pixels with the color red (value 2) in the input grid.
2.  **Initiate Flood Fill:** For *each* red pixel:
    *   Start a flood-fill operation *from the white pixel directly above the red, and another from the white pixel left of the red*.
3.  **Flood Fill Procedure (Recursive):**
    *   **Base Case:** If the current pixel is out of bounds or is *not* white (0), stop.
    *   **Recursive Step:**
        *   Change the current pixel's color to blue (1).
        *   Recursively call the flood-fill procedure on the pixel *above* (y - 1) the current pixel.
        *   Recursively call the flood-fill procedure on the pixel to the *left* (x - 1) of the current pixel.
4. **Preserve Other Colors:** All pixels that are not white or affected by the flood fill retain their original colors.
"""

import numpy as np

def flood_fill(grid, x, y):
    """
    Performs a flood fill operation, changing connected white pixels (0) to blue (1)
    upwards and leftwards. Stops when hitting non-white pixels or boundaries.
    """
    if x < 0 or x >= grid.shape[1] or y < 0 or y >= grid.shape[0] or grid[y, x] != 0:
        return

    grid[y, x] = 1
    flood_fill(grid, x - 1, y)  # Left
    flood_fill(grid, x, y - 1)  # Up

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)

    # Iterate through all pixels in the grid
    for y in range(output_grid.shape[0]):
        for x in range(output_grid.shape[1]):
            # If a red pixel is found, initiate flood fill on adjacent white pixels
            if output_grid[y, x] == 2:
                if x > 0 and output_grid[y, x-1] == 0:
                    flood_fill(output_grid, x - 1, y)  # Fill left
                if y > 0 and output_grid[y-1, x] == 0:
                    flood_fill(output_grid, x, y - 1)  # Fill above

    return output_grid