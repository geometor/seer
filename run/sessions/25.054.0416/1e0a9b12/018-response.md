# 1e0a9b12 • 018 • refine_coder

---
```python
"""
All non-white pixels move down as far as possible in their respective
columns, stacking on top of other non-white pixels or stopping at
the bottom of the grid, with precedence to lower pixels.
"""

import numpy as np

def get_movable_pixels(grid):
    """
    Identify pixels that are not white (color value 0).
    Returns a list of (row, col) tuples.
    """
    movable_pixels = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != 0:
                movable_pixels.append((r, c))
    return movable_pixels

def find_lowest_available_position(grid, r, c):
    """
    Finds the lowest available position in the column for a pixel.
    """
    new_r = r
    while new_r + 1 < grid.shape[0] and grid[new_r + 1, c] == 0:
        new_r += 1
    return new_r
    

def transform(input_grid):
    """
    Transforms the input grid by moving non-white pixels downwards.
    """
    output_grid = np.copy(input_grid)
    movable_pixels = get_movable_pixels(output_grid)

    # Sort movable pixels by row in reverse order (bottom-up)
    movable_pixels.sort(reverse=True)

    for r, c in movable_pixels:
        # Find the lowest available position in the column
        new_r = find_lowest_available_position(output_grid, r, c)

        # If the lowest position is different from the current, move the pixel
        if new_r != r:
            output_grid[new_r, c] = output_grid[r, c]
            output_grid[r, c] = 0

    return output_grid
```
