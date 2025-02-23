# 2-0ca9ddb6 • 010 • example_3 - CODE

---
```python
"""
The transformation preserves the positions of the existing red, blue, and magenta pixels and introduces new yellow pixels around each of the red pixels and orange pixels around each of the blue pixels based on their relative positions. Magenta pixels are preserved but do not generate new pixels. All other pixels remain white.
"""

import numpy as np

def find_all_pixels(grid, color):
    """Finds the coordinates of all occurrences of a specific color."""
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    
    # Find all red (2) and blue (1) pixels
    red_positions = find_all_pixels(input_grid, 2)
    blue_positions = find_all_pixels(input_grid, 1)

    # Add yellow (4) pixels around each red pixel
    for red_pos in red_positions:
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
    # Add orange (7) pixels around each blue pixel
    for blue_pos in blue_positions:
        row, col = blue_pos
        if col > 0:
            output_grid[row, col - 1] = 7  # One column left
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # One column right
        if row > 0:
            output_grid[row - 1, col] = 7  # One row above

    return output_grid
```

