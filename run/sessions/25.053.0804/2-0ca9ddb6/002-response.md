# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
1.  **Locate Key Pixels:** Find the single red pixel (value 2) and the single blue pixel (value 1) in the input grid.
2.  **Create Yellow Pixels:**
    *   Two yellow pixels are created, one row *above* the red pixel and one column to either side.
    *   Two yellow pixels are created, one row *below* the red pixel and one column to either side.
3.  **Create Orange Pixels:**
    *   One orange pixel is placed one row above the blue pixel at the blue pixel's column.
    *   Two orange pixels are created, one row *below* the blue pixel, centered on the blue pixel.
    *    One Orange pixel is placed one row below the blue pixel at the blue pixel's column.
"""

import numpy as np

def find_pixel_by_color(grid, color):
    # Find the coordinates of a single pixel of the specified color.
    indices = np.where(grid == color)
    if len(indices[0]) > 0:
        return (indices[0][0], indices[1][0])  # Return first occurrence
    return None

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the red and blue pixels.
    red_pos = find_pixel_by_color(input_grid, 2)
    blue_pos = find_pixel_by_color(input_grid, 1)

    # Create yellow pixels around the red pixel.
    if red_pos:
        row, col = red_pos
        if row > 0: #check if the row above is valid
          if col > 0:
            output_grid[row - 1, col - 1] = 4  # One row above, one column left
          if col < output_grid.shape[1] - 1:
            output_grid[row - 1, col + 1] = 4  # One row above, one column right
        if row < output_grid.shape[0] -1: #check for row below
          if col > 0:
            output_grid[row + 1, col - 1] = 4  # One row below, one column left
          if col < output_grid.shape[1] - 1:
            output_grid[row + 1, col + 1] = 4  # One row below, one column right

    # Create orange pixels around the blue pixel.
    if blue_pos:
        row, col = blue_pos
        if row > 0:  #check if the row above is valid
          output_grid[row - 1, col] = 7  # One row above, same column
        if row < output_grid.shape[0] - 1:
          output_grid[row + 1, col] = 7 #one row below, same column
        if col > 0:
          output_grid[row, col - 1] = 7  # Same row, one column left
        if col < output_grid.shape[1] - 1:
          output_grid[row, col + 1] = 7  # Same row, one column right

    return output_grid
```
