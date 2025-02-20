# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
Transformation Rule:
The azure (8) objects remain unchanged. 
A blue (1) pixel is added to the immediate right of the top of the topmost vertical azure line.
Another blue (1) pixel is added to the immediate left of the bottommost horizontal azure line.
"""

import numpy as np

def find_topmost_vertical_line(grid, color):
    """Finds the topmost vertical line of a given color."""
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                return r, c
    return None

def find_bottommost_horizontal_line(grid, color):
    """Finds the bottommost horizontal line of a given color."""
    rows, cols = grid.shape
    for r in reversed(range(1, rows)):
        for c in range(cols - 1):
            if grid[r, c] == color and grid[r, c+1] == color:
                return r, c
    return None

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid

    # Find the topmost vertical line of color 8
    top_vertical = find_topmost_vertical_line(output_grid, 8)
    if top_vertical:
        r, c = top_vertical
        # Add a blue pixel (1) to the right of the top of the line
        if c + 1 < output_grid.shape[1]: #boundary check
          output_grid[r, c + 1] = 1

    # Find the bottommost horizontal line of color 8
    bottom_horizontal = find_bottommost_horizontal_line(output_grid, 8)
    if bottom_horizontal:
        r, c = bottom_horizontal
        # Add a blue pixel (1) to the left of the line
        if c-1 >= 0:
          output_grid[r, c - 1] = 1

    return output_grid
```

