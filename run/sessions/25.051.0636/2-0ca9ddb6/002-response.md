# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
The transformation involves adding a mirrored L-shape made of yellow color above each initial red cell, and an orange cross centered on the blue cell.
"""

import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the red (color 2) and blue (color 1) cells.
    red_cells = find_objects(input_grid, 2)
    blue_cells = find_objects(input_grid, 1)

    # Add mirrored L-shape yellow marks (color 4) above the red cell.
    for red_cell in red_cells:
        y, x = red_cell
        output_grid[y - 1, x - 1] = 4
        output_grid[y - 1, x + 1] = 4

    # Add orange cross (color 7) centered on the blue cell.
    for blue_cell in blue_cells:
        y, x = blue_cell
        output_grid[y, x] = 7      # Center
        output_grid[y - 1, x] = 7  # Top
        output_grid[y + 1, x] = 7  # Bottom
        output_grid[y, x - 1] = 7  # Left
        output_grid[y, x + 1] = 7  # Right
    return output_grid
```
