# 1e32b0e9 • 006 • refine_coder

---
```python
"""
Transforms an input grid by replacing white (0) pixels that are adjacent to
any non-white pixel with azure (8). Non-white pixels remain unchanged.
"""

import numpy as np

def get_all_neighbors(grid, row, col):
    """Gets the valid neighboring coordinates of a cell, including diagonals."""
    rows, cols = grid.shape
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue  # Skip the cell itself
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                neighbors.append((new_row, new_col))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Find all pixels that are not 0 (white).
    non_zero_pixels = np.argwhere(input_grid != 0)

    # 2. Iterate through the neighbors of non-zero pixels.
    for row, col in non_zero_pixels:
        neighbors = get_all_neighbors(input_grid, row, col)
        # 3. Check if any neighbor is 0. If so, change it to 8 in the output grid.
        for nr, nc in neighbors:
            if input_grid[nr, nc] == 0:  # Only change 0 pixels
                output_grid[nr, nc] = 8

    return output_grid
```
