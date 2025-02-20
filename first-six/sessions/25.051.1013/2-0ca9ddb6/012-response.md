# 2-0ca9ddb6 • 012 • refine_code - CODE

---
```python
"""
The transformation involves identifying red (2) and blue (1) cells in the input grid. For each red cell, two yellow (4) cells are placed diagonally up-left and up-right. For each blue cell, three orange (7) cells are placed, forming an "L" shape: one to the left, one below, and one diagonally down-left. All other cells remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Finds the positions of all single-cell objects of the specified color."""
    coords = np.argwhere(grid == color)
    # Convert to list of tuples
    return [tuple(coord) for coord in coords]

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)

    # Find all red and blue cells
    red_positions = find_objects(input_grid, 2)
    blue_positions = find_objects(input_grid, 1)

    # Red cell actions: add yellow cells for each red cell
    for red_pos in red_positions:
        if red_pos[0] - 1 >= 0 and red_pos[1] - 1 >= 0:
          output_grid[red_pos[0] - 1, red_pos[1] - 1] = 4  # Up-left
        if red_pos[0] - 1 >= 0 and red_pos[1] + 1 < output_grid.shape[1]:
          output_grid[red_pos[0] - 1, red_pos[1] + 1] = 4  # Up-right

    # Blue cell actions: add orange cells in L-shape
    for blue_pos in blue_positions:
        if blue_pos[1] - 1 >= 0:
          output_grid[blue_pos[0] , blue_pos[1] - 1] = 7 # left
        if blue_pos[0] + 1 < output_grid.shape[0] and blue_pos[1] - 1 >=0:
          output_grid[blue_pos[0] + 1, blue_pos[1] - 1] = 7 #bottom-left
        if blue_pos[0] + 1 < output_grid.shape[0]:
          output_grid[blue_pos[0] + 1, blue_pos[1]] = 7 # bottom

    return output_grid
```

