# 99fa7670 • 010 • refine_coder

---
```python
"""
Finds all non-black (non-zero) pixels in the input grid and propagates their color to the cells to the right and below them, effectively filling rectangles.
"""

import numpy as np

def find_seed_pixels(grid):
    # Find the coordinates of all non-black pixels.
    seed_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
            if pixel != 0:
                seed_pixels.append((row_index, col_index))
    return seed_pixels

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find all non-black seed pixels.
    seed_pixels = find_seed_pixels(input_grid)

    # Iterate through each seed pixel and propagate its color.
    for row, col in seed_pixels:
        color = input_grid[row, col]

        # Propagate to the right.
        output_grid[row, col:] = color

        # Propagate below.
        output_grid[row:, col] = color
    
    return output_grid
```
