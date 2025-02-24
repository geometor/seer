# 99fa7670 • 012 • refine_coder

---
```python
"""
Finds all non-black (non-zero) pixels in the input grid. Each non-black pixel
acts as the top-left corner of a rectangle. The rectangle extends to the right
and down until another non-black pixel or the edge of the grid is encountered.
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
    seed_pixels.sort() #ensure top-left processing

    # Iterate through each seed pixel and propagate its color.
    for row, col in seed_pixels:
        color = input_grid[row, col]

        # Propagate to the right, stopping at the next seed pixel or boundary
        for c in range(col + 1, output_grid.shape[1]):
            if output_grid[row,c] != 0:
                break  # Stop at next seed
            output_grid[row, c] = color

        # Propagate downwards, stopping at the next seed pixel of boundary
        for r in range(row + 1, output_grid.shape[0]):
            if output_grid[r,col] != 0:
                break  #Stop at next seed
            output_grid[r,col] = color
            
        output_grid[row,col] = color # set the seed itself

    return output_grid
```
