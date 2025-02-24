# e179c5f4 • 010 • refine_coder

---
```python
"""
Finds the '1' pixel in the input grid and replaces all '0' pixels with a checkerboard pattern of '8' and '1' values, radiating outwards from the location of the initial '1' pixel, such that the '1' pixel is considered a corner of the radiating pattern.
"""

import numpy as np

def find_pixel(grid, value):
    # Find the coordinates of the pixel with the specified value.
    for r, row in enumerate(grid):
        for c, pixel in enumerate(row):
            if pixel == value:
                return (r, c)
    return None

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the coordinates of the '1' pixel.
    blue_pixel_coords = find_pixel(input_grid, 1)
    if blue_pixel_coords is None:
        return output_grid #should not happen based on prior
    blue_row, blue_col = blue_pixel_coords

    # Iterate through the grid and apply the checkerboard pattern, relative to blue pixel.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0:
                # Calculate the distance from blue
                row_dist = abs(r - blue_row)
                col_dist = abs(c - blue_col)
                if (row_dist + col_dist) % 2 == 0:
                    output_grid[r, c] = 8
                else:
                    output_grid[r, c] = 1

    return output_grid
```
