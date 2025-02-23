# 2-0ca9ddb6 • 002 • Response

---

*text:*

```python
"""
The transformation rule involves drawing a yellow cross above the red cell and an orange cross around the blue cell. The original cells remain, other positions remain unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-cell object with the given color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return the first occurrence
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the red object (color 2)
    red_pos = find_object(input_grid, 2)
    if red_pos:
        # Create the yellow cross one cell above red
        row, col = red_pos
        output_grid[row - 1 , col - 1] = 4
        output_grid[row - 1, col + 1] = 4
        output_grid[row - 2, col]     = 4 # cell above
        output_grid[row, col ]       = 2 # preserve location
        # output_grid[row - 1, col] = 4 # cell above, removed
        # output_grid[row + 1, col] = 4 # cell below, removed

    # Find the blue object (color 1)
    blue_pos = find_object(input_grid, 1)
    if blue_pos:
        # Create the orange cross around blue
        row, col = blue_pos
        output_grid[row - 1, col] = 7
        output_grid[row + 1, col] = 7
        output_grid[row, col - 1] = 7
        output_grid[row, col + 1] = 7

    return output_grid
```

