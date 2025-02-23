# 0a938d79 • 010 • example_2 - CODE

---
```python
"""
The transformation takes the initial positions of colored pixels (blue and green) and uses them as starting points to create a horizontally and vertically repeating pattern, keeping all other positions in the grid white. The horizontal pattern expands from the initial color, while the vertical replicates every horizontal colored pixel.
"""

import numpy as np

def get_colored_pixels(grid, color):
    # Find coordinates of pixels of a specific color.
    return np.argwhere(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find initial positions of blue and green pixels.
    blue_pixels = get_colored_pixels(input_grid, 1)
    green_pixels = get_colored_pixels(input_grid, 3)
    
    # set all values to 0 that are not 1 or 3
    for r in range(rows):
      for c in range(cols):
        if input_grid[r][c] != 1 and input_grid[r][c] != 3:
          input_grid[r][c] = 0

    # Horizontal and Vertical Replication for Blue Pixels.
    for r, c in blue_pixels:
        for j in range(c, cols, 6):
            for i in range(rows):
                output_grid[i, j] = 1

    # Horizontal and Vertical Replication for Green Pixels.
    for r, c in green_pixels:
        for j in range(c, cols, 6):
            for i in range(rows):
                output_grid[i, j] = 3

    return output_grid.tolist()
```
