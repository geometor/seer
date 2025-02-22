# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
The transformation preserves the positions of the existing red and blue pixels and introduces new yellow pixels around the red pixel and orange pixels around the blue pixel based on their relative positions. The rest of the pixels stay white.
"""

import numpy as np

def find_pixel(grid, color):
    """Finds the coordinates of the first occurrence of a specific color."""
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])
    return None

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    
    # Find the red (2) and blue (1) pixels
    red_pos = find_pixel(input_grid, 2)
    blue_pos = find_pixel(input_grid, 1)

    # Add yellow (4) pixels around the red pixel
    if red_pos:
        row, col = red_pos
        if row > 0:
          if col > 0:
            output_grid[row - 1, col - 1] = 4  # One row above, one column left
          if col < output_grid.shape[1]-1:  
            output_grid[row - 1, col + 1] = 4  # One row above, one column right
        if row < output_grid.shape[0]-1:
          if col > 0:
             output_grid[row + 1, col - 1] = 4
          if col < output_grid.shape[1]-1:
            output_grid[row + 1, col + 1] = 4
    # Add orange (7) pixels around the blue pixel
    if blue_pos:
        row, col = blue_pos
        if col > 0:
            output_grid[row, col - 1] = 7  # One column left
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # One column right
        if row > 0:
            output_grid[row - 1, col] = 7  # One row above

    return output_grid
```

