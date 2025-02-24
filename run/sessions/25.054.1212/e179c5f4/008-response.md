# e179c5f4 • 008 • example_2 • investigate_coder

---
```python
"""
Finds the '1' pixel in the input grid and replaces all '0' pixels with a checkerboard pattern of '8' and '1' values, radiating outwards from the location of the initial '1' pixel.
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

    # Iterate through the grid and apply the checkerboard pattern.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0:
                if (r + c) % 2 == (blue_row + blue_col) % 2:
                    output_grid[r, c] = 8
                else:
                    output_grid[r, c] = 1

    return output_grid
```
