# 2-0ca9ddb6 • 004 • example_2 - CODE

---
```python
"""
1.  **Copy Azure Pixel:**  Copy the azure pixel from the input to the same position in the output grid.
2.  **Locate Red Pixels:** Find all red pixels (value 2) in the input grid.
3.  **Create Yellow Pixels (for each red pixel):**
    *   Two yellow pixels are created, one row *above* the red pixel and one column to either side.
    *   Two yellow pixels are created, one row *below* the red pixel and one column to either side.
4.  **Locate Blue Pixels:** Find all blue pixels (value 1) in the input grid.
5.  **Create Orange Pixels (for each blue pixel):**
    *   One orange pixel is placed one row above the blue pixel at the blue pixel's column.
    *   One orange pixel is placed one row below the blue pixel at the blue pixel's column.
    *   Two orange pixels are created in the same row as the blue pixel, one column to the left and right.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    # Find the coordinates of all pixels of the specified color.
    indices = np.where(grid == color)
    return list(zip(indices[0], indices[1]))

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the red and blue pixels.
    red_pixels = find_pixels_by_color(input_grid, 2)
    blue_pixels = find_pixels_by_color(input_grid, 1)

    # Create yellow pixels around each red pixel.
    for red_pos in red_pixels:
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

    # Create orange pixels around each blue pixel.
    for blue_pos in blue_pixels:
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

