# 2-0ca9ddb6 • 004 • refine_code - CODE

---
```python
"""
Copies a red and blue pixel from the input grid to the output grid. Adds yellow pixels above and below the red pixel and orange pixels surrounding the blue pixel.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-cell object of the specified color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the defined rules:
    1. Copies the red (2) and blue (1) pixels.
    2. Adds yellow (4) pixels above and below the red pixel.
    3. Adds orange (7) pixels around the blue pixel.
    """
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the red and blue pixels
    red_pos = find_object(input_grid, 2)
    blue_pos = find_object(input_grid, 1)

    # Copy red pixel
    if red_pos:
      output_grid[red_pos] = 2

    # Copy blue pixel
    if blue_pos:
        output_grid[blue_pos] = 1


    # Add yellow pixels above and below the red pixel
    if red_pos:
        row, col = red_pos
        if row > 0:  # Check for upper boundary
            output_grid[row - 1, col] = 4
        if row < rows - 1:  # Check for lower boundary
            output_grid[row + 1, col] = 4

    # Add orange pixels around the blue pixel
    if blue_pos:
        row, col = blue_pos
        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                output_grid[i, j] = 7

    return output_grid
```

