# aedd82e4 • 012 • refine_coder

---
```python
"""
Identify all red pixels within the input grid.
Identify all white pixels.
Identify all white pixels that are *diagonally adjacent* to red pixels, traveling down and to the right *from* the red pixels.
Change the color of the selected white pixels from white (0) to blue (1).
Preserve the color and position of all other pixels (red and the remaining white).
"""

import numpy as np

def get_red_pixels(grid):
    # Find coordinates of all red pixels (value 2).
    red_pixels = []
    for row_idx, row in enumerate(grid):
        for col_idx, pixel in enumerate(row):
            if pixel == 2:
                red_pixels.append((row_idx, col_idx))
    return red_pixels

def get_white_pixels(grid):
    # Find coordinates of all white pixels
    white_pixels = []
    for row_idx, row in enumerate(grid):
        for col_idx, pixel in enumerate(row):
            if pixel == 0:
                white_pixels.append((row_idx, col_idx))
    return white_pixels

def get_diagonally_adjacent_down_right(grid, red_pixels):
    # Find white pixels diagonally adjacent (down-right) to red pixels.

    adjacent_pixels = []
    rows = len(grid)
    cols = len(grid[0])

    for r_row, r_col in red_pixels:
      target_row = r_row + 1
      target_col = r_col + 1

      if 0 <= target_row < rows and 0 <= target_col < cols:
          adjacent_pixels.append((target_row, target_col))
    return adjacent_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find red pixels.
    red_pixels = get_red_pixels(input_grid)

    # find white pixels
    white_pixels = get_white_pixels(input_grid)
    
    # Find diagonally adjacent pixels
    down_right_adjacent = get_diagonally_adjacent_down_right(input_grid, red_pixels)

    # change output pixels
    for row, col in down_right_adjacent:
        if output_grid[row, col] == 0:
           output_grid[row, col] = 1

    return output_grid
```
