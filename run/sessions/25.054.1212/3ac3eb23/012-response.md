# 3ac3eb23 • 012 • refine_coder

---
```python
"""
1. Find Seed Pixel: Locate the first non-black pixel in the input grid. This is the "seed" pixel.
2. Blacken Seed: Change the color of the seed pixel to black (0).
3. Preserve Row: The original values of all pixels in the same row as the seed pixel must be unchanged.
4. Draw Vertical Line: Draw a vertical line through the seed pixel's column.
5. Color Vertical Line: The color of each pixel in the vertical line is determined by the original pixel color in that row in the input grid. If the original input grid has a non-black pixel at the location of the vertical line, the output grid's pixel in the vertical line will have that same color. If the location is black in the input grid, the output pixel is also black.
"""

import numpy as np

def find_seed_pixel(grid):
    # Find the coordinates of the first non-black pixel.
    for r, row in enumerate(grid):
        for c, pixel in enumerate(row):
            if pixel != 0:
                return (r, c)
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    
    # Find the seed pixel (the first non-black pixel).
    seed_location = find_seed_pixel(input_grid)

    if seed_location is None:
        return output_grid # returns the input_grid unchanged
    
    seed_row, seed_col = seed_location

    # Change seed pixel to black
    output_grid[seed_row, seed_col] = 0

    # Draw the vertical line, inheriting color from the corresponding row in the input.
    for r in range(output_grid.shape[0]):
        output_grid[r, seed_col] = input_grid[r, seed_col]

    return output_grid
```
