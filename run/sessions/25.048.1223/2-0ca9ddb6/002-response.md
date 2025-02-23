# 2-0ca9ddb6 • 002 • Response

---

*text:*

```python
"""
The transformation preserves a red cell and a blue cell. Then, it draws a yellow, symmetrical aura one cell distant to the red object and an orange aura one cell distant to the blue object.
"""

import numpy as np

def find_object(grid, color):
    """Finds the position of a single-cell object of a given color."""
    coords = np.argwhere(grid == color)
    if coords.size > 0:
        return tuple(coords[0])
    return None

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the red object (color 2)
    red_pos = find_object(input_grid, 2)
    if red_pos:
        # Create yellow aura around the red object
        row, col = red_pos
        if row > 0:
            output_grid[row - 1, col-1] = 4  # top left
            output_grid[row - 1, col+1] = 4  # top right
        if row < output_grid.shape[0] -1:
            output_grid[row+1, col-1] = 4 # bottom left
            output_grid[row+1, col+1] = 4 # bottom right

    # Find the blue object (color 1)
    blue_pos = find_object(input_grid, 1)
    if blue_pos:
        # Create orange aura around the blue object
        row, col = blue_pos
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # Right
        if row < output_grid.shape[0] - 1:
            output_grid[row + 1, col] = 7  # Down
        if row > 0:
            output_grid[row - 1, col] = 7 # Up

    return output_grid
```

