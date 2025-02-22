# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
The single red object in the input gets a yellow object as its "shadow".
The single blue object in the input gets an orange "cross" surrounding it.
"""

import numpy as np

def find_object(grid, color):
    # Find the position of a single-cell object with the given color.
    positions = np.argwhere(grid == color)
    return positions[0] if positions.size > 0 else None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find the position of the red object (color 2).
    red_pos = find_object(input_grid, 2)
    if red_pos is not None:
        # Create two yellow "L" shape.
        output_grid[red_pos[0] - 1, red_pos[1] - 1] = 4
        output_grid[red_pos[0] - 1, red_pos[1] + 1] = 4
        output_grid[red_pos[0] + 1, red_pos[1] - 1] = 4
        output_grid[red_pos[0] + 1, red_pos[1] + 1] = 4
        

    # Find the position of the blue object (color 1).
    blue_pos = find_object(input_grid, 1)
    if blue_pos is not None:
        # Create an orange cross around the blue object.
        output_grid[blue_pos[0] - 1, blue_pos[1]] = 7
        output_grid[blue_pos[0] + 1, blue_pos[1]] = 7
        output_grid[blue_pos[0], blue_pos[1] - 1] = 7
        output_grid[blue_pos[0], blue_pos[1] + 1] = 7

    return output_grid
```

