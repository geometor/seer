"""
1. **Identify Key Pixels:** Locate the pixel with the value '6' (magenta) and the pixel with the value '4' (yellow) and the pixel with the value 3 (green).
2.  **Preserve Key Pixels and other non-zero pixels:** The original colored values are unchanged in terms of location.
3.  **Propagate Magenta (6):** All pixels below the magenta pixel, including diagonal pixels, are changed to the value '6'.
4. **Propagate Yellow (4)**: All pixels below the yellow pixel are change to the value '4'.
5. **Preserve the rest:** Leave all the rest of the original grid intact.
"""

import numpy as np

def find_pixel(grid, value):
    """Finds the location of a pixel with a specific value."""
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == value:
                return (i, j)
    return None

def transform(input_grid):
    """Transforms the input grid according to the cascading fill-down rule."""
    output_grid = np.copy(input_grid)  # Initialize output grid as a copy

    # Find the locations of pixels with values 6 and 4.
    loc_6 = find_pixel(input_grid, 6)
    loc_4 = find_pixel(input_grid, 4)
    loc_3 = find_pixel(input_grid,3)

    # Propagate 6 downwards and diagonally.
    if loc_6:
        for i in range(loc_6[0] + 1, output_grid.shape[0]):
            for j in range(output_grid.shape[1]):
               output_grid[i,j] = 6

    if loc_4:
        for i in range(loc_4[0] + 1, output_grid.shape[0]):
          output_grid[i,loc_4[1]] = 4

    return output_grid