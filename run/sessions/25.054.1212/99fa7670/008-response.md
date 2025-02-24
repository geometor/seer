# 99fa7670 • 008 • example_2 • investigate_coder

---
```python
"""
Finds the magenta (color 6) pixel in the input grid and propagates the color to the cells directly to the right and below it.
"""

import numpy as np

def find_magenta_pixel(grid):
    # Find the coordinates of the magenta pixel (color 6).
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
            if pixel == 6:
                return (row_index, col_index)
    return None  # Return None if no magenta pixel is found

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find the magenta pixel.
    magenta_pixel_coords = find_magenta_pixel(input_grid)

    # If a magenta pixel is found, propagate the color.
    if magenta_pixel_coords:
        row, col = magenta_pixel_coords

        # Propagate to the right, boundary check
        if col + 1 < output_grid.shape[1]:
            output_grid[row, col + 1] = 6

        # Propagate below, boundary check
        if row + 1 < output_grid.shape[0]:
            output_grid[row + 1, col] = 6
    
    return output_grid
```
