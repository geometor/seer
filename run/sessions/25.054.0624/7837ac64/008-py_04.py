"""
1. **Identify and Isolate:** Scan the input grid and identify all pixels that are *not* green (3) or white (0). In this case, find the red (2) and azure (8) pixels.
2. **Extreme Down-sampling:** Create a new, much smaller 3x3 grid.
3. **Map and reconstruct (condense):** Place the identified non-green, non-white colors (red and azure) into the new grid, maintaining approximate relative positioning from input. The other cells are filled with white (0). Because the grid has been reduced, the location is based on groups of 9 input cells.
"""

import numpy as np

def find_non_background_pixels(grid):
    """Finds the coordinates and colors of pixels that are not green (3) or white (0)."""
    non_background_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
            if pixel != 3 and pixel != 0:
                non_background_pixels.append(((row_index, col_index), pixel))
    return non_background_pixels

def transform(input_grid):
    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Find non-background pixels (not green or white)
    non_background_pixels = find_non_background_pixels(input_grid)

    # Map the found pixels to the 3x3 grid
    for (row, col), color in non_background_pixels:
        # Determine the corresponding position in the output grid (integer division by 9 for this specific case)
        output_row = row // (input_grid.shape[0] // 3)
        output_col = col // (input_grid.shape[1] // 3)

        # check bounds - important to prevent errors in other examples
        if output_row < output_grid.shape[0] and output_col < output_grid.shape[1]:
          output_grid[output_row, output_col] = color

    return output_grid