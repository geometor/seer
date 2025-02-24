# f2829549 • 012 • refine_coder

---
```python
"""
The output grid's height is the same as the input grid's height. The output
grid's width is one less than the input grid height.  The output is a
checkerboard pattern of alternating white (0) and green (3) pixels, starting
with white (0) in the top-left cell.
"""

import numpy as np

def build_checkerboard(rows, cols, start_color, other_color):
    """Builds a checkerboard pattern."""
    grid = np.zeros((rows, cols), dtype=int)
    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 == 0:
                grid[r, c] = start_color
            else:
                grid[r, c] = other_color
    return grid
    

def transform(input_grid):
    # initialize output_grid
    input_rows, input_cols = input_grid.shape
    output_rows = input_rows
    output_cols = input_rows - 1 # Output width is input_height - 1

    # Create a checkerboard with white and green, starting with white
    output_grid = build_checkerboard(output_rows, output_cols, 0, 3)

    return output_grid
```
