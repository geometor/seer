# 2-0ca9ddb6 • 004 • Response

---

*text:*

```python
"""
The transformation preserves the azure, red, and blue cells in their initial positions. It creates a yellow aura (color 4) one cell distant to the left and to the right of the red objects, and it creates an orange aura (color 7) one cell to the left, right, and below for the blue objects and one up.
"""

import numpy as np

def find_object(grid, color):
    """Finds the positions of all single-cell objects of a given color."""
    coords = np.argwhere(grid == color)
    return [tuple(coord) for coord in coords]

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the red objects (color 2)
    red_positions = find_object(input_grid, 2)
    for red_pos in red_positions:
        # Create yellow aura around the red objects
        row, col = red_pos
        if col > 0:
            output_grid[row, col - 1] = 4  # Left
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 4  # Right

    # Find the blue objects (color 1)
    blue_positions = find_object(input_grid, 1)
    for blue_pos in blue_positions:
        # Create orange aura around the blue objects
        row, col = blue_pos
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # Right
        if row < output_grid.shape[0] - 1:
            output_grid[row + 1, col] = 7  # Down
        if row > 0:
            output_grid[row-1,col] = 7 # Up

    return output_grid
```

