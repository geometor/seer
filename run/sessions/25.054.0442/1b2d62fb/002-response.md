# 1b2d62fb • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule detects a vertical line of blue (1) pixels, collapses the grid horizontally, and replaces the detected feature with a horizontal line of azure (8) pixels in the fourth row. The rest of the output grid is filled with white (0) pixels.
"""

import numpy as np

def find_vertical_line(grid, color):
    """Finds the column index of a vertical line of the specified color."""
    height, width = grid.shape
    for j in range(width):
        is_line = True
        for i in range(height):
            if grid[i, j] != color:
                is_line = False
                break
        if is_line:
            return j
    return -1  # Return -1 if no such line is found

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    # Find the vertical blue line
    blue_column = find_vertical_line(input_grid, 1)

    # Initialize the output grid (5x3, filled with 0s)
    output_grid = np.zeros((5, 3), dtype=int)

    # Condense and place the azure line in the output grid at row index 3 (fourth row)
    if blue_column != -1:
        output_grid[3, :] = 8

    return output_grid
```
