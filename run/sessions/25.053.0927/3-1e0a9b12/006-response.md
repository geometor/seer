# 3-1e0a9b12 • 006 • example_3 - CODE

---
```python
"""
Shift all non-zero pixels down by two rows. If a pixel reaches the bottom edge, it stops. If pixels collide, the top pixel is moved one row above where it would collide.
"""

import numpy as np

def get_nonzero_pixels(grid):
    pixels = []
    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value != 0:
                pixels.append({
                    'value': value,
                    'row': row_idx,
                    'col': col_idx
                })
    return pixels

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid, then modify.
    output_grid = np.zeros_like(input_grid)
    input_pixels = get_nonzero_pixels(input_grid)

    # Create a dictionary to track occupied cells in the output grid.
    occupied = {}

    for pixel in input_pixels:
        value = pixel['value']
        row = pixel['row']
        col = pixel['col']

        # Attempt to shift down by two rows.
        new_row = row + 2

        # Check bounds.
        if new_row >= input_grid.shape[0]:
            new_row = row + 1
            if new_row >= input_grid.shape[0]:
                new_row = row

        # Check for collisions and adjust. Do this before placing.
        if (new_row, col) in occupied:
            new_row -= 1

        # Place the pixel in output after checks
        output_grid[new_row, col] = value
        occupied[(new_row, col)] = True

    return output_grid
```
