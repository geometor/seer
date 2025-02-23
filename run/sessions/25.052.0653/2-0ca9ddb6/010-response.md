# 2-0ca9ddb6 • 010 • example_3 - CODE

---
```python
"""
Copies red, blue, and magenta pixels from the input grid to the output grid. Adds yellow pixels above and below the red pixel and orange pixels surrounding the blue pixel.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all single-cell objects of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """
    Transforms the input grid according to the defined rules:
    1. Copies red (2), blue (1), and magenta (6) pixels.
    2. Adds yellow (4) pixels above and below the red pixel.
    3. Adds orange (7) pixels around the blue pixel.
    """
    output_grid = np.copy(input_grid)

    # Find the red, blue and magenta pixels
    red_pixels = find_objects(input_grid, 2)
    blue_pixels = find_objects(input_grid, 1)
    magenta_pixels = find_objects(input_grid, 6)

    # Copy red, blue and magenta pixels
    for pos in red_pixels:
        output_grid[pos] = 2
    for pos in blue_pixels:
        output_grid[pos] = 1
    for pos in magenta_pixels:
        output_grid[pos]= 6

    # Add yellow pixels above and below the red pixel
    for row, col in red_pixels:
        if row > 0:
          output_grid[row - 1, col-1] = 4
          output_grid[row - 1, col+1] = 4
        if row < output_grid.shape[0] - 1:
          output_grid[row + 1, col-1] = 4
          output_grid[row + 1, col+1] = 4

    # Add orange pixels around the blue pixel
    for row, col in blue_pixels:
        for i in range(row - 1, row + 2):
            if 0 <= i < output_grid.shape[0]:
                output_grid[i, col] = 7
        for j in range(col - 1, col + 2):
            if 0 <= j < output_grid.shape[1]:
                output_grid[row, j] = 7

    return output_grid
```

