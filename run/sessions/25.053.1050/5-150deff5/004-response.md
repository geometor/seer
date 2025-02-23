# 5-150deff5 • 004 • refine_coder

---
```python
"""
The transformation rule is as follows:
1. Identify contiguous shapes of gray (5) pixels in the input grid.
2. Outline the outermost layer of the shape:
   - A gray pixel is considered part of the outline if it is directly adjacent (up, down, left, or right) to a pixel that is *not* gray (including out-of-bounds).
   - Replace these outline pixels with azure (8).
3. Fill the interior of the outlined shape:
   - Any gray pixel that is *not* part of the outline is considered interior.
   - Replace these interior pixels with red (2).
4. Preserve the white (0) background.
"""

import numpy as np

def is_part_of_shape(grid, r, c, shape_color):
    """Checks if a pixel is within bounds and of the specified color."""
    rows, cols = grid.shape
    return 0 <= r < rows and 0 <= c < cols and grid[r, c] == shape_color

def is_outermost(grid, row, col, shape_color):
    """
    Checks if a pixel at (row, col) is on the outermost layer of the shape.
    A pixel is outermost if it's part of the shape and has at least one 
    neighbor (up, down, left, right) that is not part of the shape.
    """
    rows, cols = grid.shape
    if not is_part_of_shape(grid, row, col, shape_color):
        return False

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if not is_part_of_shape(grid, nr, nc, shape_color):
            return True  # Directly adjacent to a non-shape pixel or edge

    return False

def transform(input_grid):
    # Initialize output_grid with the same dimensions and background as input_grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    shape_color = 5

    # Iterate through all pixels to find and process the shape.
    for row in range(rows):
        for col in range(cols):
            if is_outermost(input_grid, row, col, shape_color):
                output_grid[row, col] = 8  # Azure for outline
            elif input_grid[row,col] == shape_color:
                output_grid[row, col] = 2  # Red for fill

    return output_grid
```
