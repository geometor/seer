# 2-0ca9ddb6 • 010 • example_3 - CODE

---
```python
"""
The transformation rule involves creating a yellow cross around each red cell and placing orange cells around each blue cell in the cardinal directions.

1. Copy the input grid to the output grid.
2. Find all red (2) and blue (1) cells in the input grid.
3. For each red cell:
    - Place a yellow (4) cell one position above, below, to the left, and to the right.
4. For each blue cell:
    - Place an orange (7) cell one position above, below, to the left, and to the right.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all single-cell objects of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find all red (2) and blue (1) cells.
    red_positions = find_objects(input_grid, 2)
    blue_positions = find_objects(input_grid, 1)

    # Create yellow crosses around each red cell.
    for y, x in red_positions:
        if y > 0:
            output_grid[y-1, x] = 4  # Above
        if y < output_grid.shape[0]-1:
            output_grid[y+1, x] = 4  # Below
        if x > 0:
            output_grid[y, x-1] = 4  # Left
        if x < output_grid.shape[1]-1:
            output_grid[y, x+1] = 4  # Right

    # Create orange surrounds for each blue cell.
    for y, x in blue_positions:
        if y > 0:
            output_grid[y-1, x] = 7  # Above
        if y < output_grid.shape[0]-1:
            output_grid[y+1, x] = 7  # Below
        if x > 0:
            output_grid[y, x-1] = 7  # Left
        if x < output_grid.shape[1]-1:
            output_grid[y, x+1] = 7  # Right

    return output_grid
```

