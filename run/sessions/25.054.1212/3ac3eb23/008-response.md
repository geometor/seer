# 3ac3eb23 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule involves identifying the location of a single yellow (4) pixel in the input grid and then drawing a horizontal and a vertical line of yellow pixels centered on that location, extending to the edges of the grid.
"""

import numpy as np

def find_seed_pixel(grid, color=4):
    # Find the coordinates of the specified color pixel.
    for r, row in enumerate(grid):
        for c, pixel in enumerate(row):
            if pixel == color:
                return (r, c)
    return None  # Should not happen in this specific task, but good practice.

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    
    # Find the seed pixel (the original yellow pixel).
    seed_location = find_seed_pixel(input_grid)

    if seed_location is None:
        return output_grid # returns the input_grid unchanged
    
    seed_row, seed_col = seed_location

    # Draw the vertical line.
    for r in range(output_grid.shape[0]):
        output_grid[r, seed_col] = 4

    # Draw the horizontal line.
    for c in range(output_grid.shape[1]):
        output_grid[seed_row, c] = 4

    return output_grid
```
