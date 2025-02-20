# 2-0ca9ddb6 • 004 • refine_code - CODE

---
```python
"""
The transformation involves identifying a red cell (color 2) and a blue cell (color 1). A 2x2 square of yellow cells (color 4) is formed around the red cell, and an "L" shape of orange cells (color 7) is formed around the blue cell.  The yellow and orange cells are placed only where no cells where present on the input_grid.
"""

import numpy as np

def find_object(grid, color):
    """Finds the position of a single-cell object of the specified color."""
    coords = np.argwhere(grid == color)
    if coords.size > 0:
        return tuple(coords[0])
    return None

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    red_pos = find_object(input_grid, 2)
    blue_pos = find_object(input_grid, 1)

    # Yellow square around red
    if red_pos:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0):
                    new_row, new_col = red_pos[0] + i, red_pos[1] + j
                    if 0 <= new_row < rows and 0 <= new_col < cols and output_grid[new_row,new_col] == 0:
                        output_grid[new_row, new_col] = 4

    # Orange L around blue
    if blue_pos:
        #Define relative positions for the "L" shape
        l_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),(1,-1),(1,0),(1,1)]
        for dr, dc in l_positions:

            new_row, new_col = blue_pos[0] + dr, blue_pos[1] + dc
             # Check boundaries and empty cells
            if 0 <= new_row < rows and 0 <= new_col < cols :
                if (dr != 0 or dc != 0) and output_grid[new_row, new_col] == 0:
                  output_grid[new_row,new_col]=7
    return output_grid
```

