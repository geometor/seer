# 1e0a9b12 • 014 • example_3 • investigate_coder

---
```python
"""
Pixels of certain colors move downwards until they encounter another non-zero pixel or the bottom of the grid.
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

def can_move_down(grid, r, c):
    """
    Checks if the pixel at (r, c) can move down.
    Returns True if the cell below is white (0) and within bounds, False otherwise.
    """
    if r + 1 < grid.shape[0]:
        return grid[r + 1, c] == 0
    return False

def move_pixel_down(grid, r, c):
    """
    Moves the pixel at (r, c) down to the next available white cell.
    """
    new_r = r + 1
    while new_r < grid.shape[0] and grid[new_r, c] == 0:
        new_r += 1
    new_r -= 1  # Move back to the last empty cell
    grid[new_r, c] = grid[r, c]
    grid[r, c] = 0
    return grid

def transform(input_grid):
    """
    Transforms the input grid by moving non-white pixels downwards until they 
    encounter an obstacle or the bottom of the grid.
    """
    output_grid = np.copy(input_grid)
    movable_pixels = get_movable_pixels(output_grid)

    # Sort movable pixels by row to simulate top-down precedence
    movable_pixels.sort()

    for r, c in movable_pixels:
      if(can_move_down(output_grid, r, c)):
        output_grid = move_pixel_down(output_grid, r, c)
    
    return output_grid
```
