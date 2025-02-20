# 2-0ca9ddb6 • 006 • example_3 - CODE

---
```python
"""
The transformation uses each red and blue cell in the input as anchor points to create new colored cells in the output. Yellow cells are placed relative to each red cell, and orange cells cluster around each blue cell. The positions of the original red, magenta, and blue cells are unchanged.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all instances of a specific color in the grid.
    coords = np.argwhere(grid == color)
    return coords.tolist() if coords.size > 0 else []

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = input_grid.copy()

    # Find all red (color 2) and blue (color 1) cells.
    red_positions = find_objects(input_grid, 2)
    blue_positions = find_objects(input_grid, 1)

    # Place yellow cells relative to each red cell.
    for red_pos in red_positions:
        yellow_row = red_pos[0] - 2
        if yellow_row >= 0:
            output_grid[yellow_row, red_pos[1]] = 4
            #check for index out of bounds
            if red_pos[1] + 2 < output_grid.shape[1]:
                output_grid[yellow_row, red_pos[1] + 2] = 4
        yellow_row = red_pos[0] - 1
        if yellow_row-1 >= 0:
          output_grid[yellow_row-1, red_pos[1]] = 4
          #check for index out of bounds
          if red_pos[1] + 2 < output_grid.shape[1]:
            output_grid[yellow_row-1, red_pos[1] + 2] = 4

    # Create orange cells around each blue cell.
    for blue_pos in blue_positions:
        #check for index out of bounds
        if blue_pos[1] - 1 >= 0:
            output_grid[blue_pos[0], blue_pos[1] - 1] = 7  # Left
        if blue_pos[1] + 1 < output_grid.shape[1]:
            output_grid[blue_pos[0], blue_pos[1] + 1] = 7  # Right
        if blue_pos[0] + 1 < output_grid.shape[0]:
            output_grid[blue_pos[0] + 1, blue_pos[1]] = 7  # Down
            output_grid[blue_pos[0] + 1, blue_pos[1] + 0] = 7 #Added +0 to avoid overwrite
        # Added this:
        if blue_pos[0] + 1 < output_grid.shape[0] and blue_pos[1] - 1 >= 0 :
            output_grid[blue_pos[0] + 1, blue_pos[1] -1] = 7

    return output_grid
```

