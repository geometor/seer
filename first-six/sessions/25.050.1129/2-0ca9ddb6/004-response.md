# 2-0ca9ddb6 • 004 • example_2 - CODE

---
```python
"""
The transformation identifies all red (2) and blue (1) cells in the input grid.
It preserves these cells, and any other non-zero cells, in the output.
A yellow (4) cross is created around each red cell, and an orange (7) cross is created around each blue cell.
The crosses are formed by placing the respective colors one cell away in each cardinal direction (up, down, left, right).
"""

import numpy as np

def find_all_objects(grid, color):
    # Find the coordinates of all single-cell objects of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    grid_size = input_grid.shape

    # Find all red and blue cells.
    red_positions = find_all_objects(input_grid, 2)
    blue_positions = find_all_objects(input_grid, 1)
    
    # Create yellow crosses around red cells.
    for row, col in red_positions:
      if row > 0:
        output_grid[row-1, col] = 4
      if row < grid_size[0] -1:
        output_grid[row+1, col] = 4
      if col > 0:
        output_grid[row, col-1] = 4
      if col < grid_size[1] - 1:
        output_grid[row, col+1] = 4

    # Create orange crosses around blue cells.
    for row, col in blue_positions:
      if row > 0:
        output_grid[row - 1, col] = 7
      if row < grid_size[0] - 1:
        output_grid[row + 1, col] = 7
      if col > 0:
        output_grid[row, col-1] = 7
      if col < grid_size[1] - 1:
          output_grid[row, col + 1] = 7      

    return output_grid
```

