# 3618c87e • 004 • refine_coder

---
```python
"""
1.  Identify all blue (color 1) pixels within the input grid.
2.  For each blue pixel:
    *   Check if there's a gray pixel (color 5) directly below it.
    *   If a gray pixel is directly below, swap the colors of the blue pixel and the gray pixel.
3.  The bottom row will reflect these swaps, and no longer be all grey.
"""

import numpy as np

def find_all_pixels_by_color(grid, color):
    # Find the coordinates of all pixels of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find all blue (1) pixels
    blue_pixel_coords = find_all_pixels_by_color(input_grid, 1)

    for blue_pixel in blue_pixel_coords:
        # Calculate coordinates of the pixel below
        row_below = blue_pixel[0] + 1
        col_same = blue_pixel[1]

        # Check if the pixel below is within bounds and is gray (5)
        if row_below < output_grid.shape[0] and output_grid[row_below, col_same] == 5:
            # Swap colors
            output_grid[blue_pixel[0], blue_pixel[1]] = 5
            output_grid[row_below, col_same] = 1

    return output_grid
```
