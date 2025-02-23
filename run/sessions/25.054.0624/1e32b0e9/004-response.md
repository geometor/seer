# 1e32b0e9 • 004 • refine_coder

---
```python
"""
Transforms an input grid by replacing all pixels adjacent to a "target" color
with azure (8). The target color is any color other than 0 in the input grid.
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

    # 1. Find "target" pixels (any non-0 color)
    target_pixels = np.argwhere(input_grid != 0)

    # 2. Iterate through neighbors of target pixels and change color
    for row, col in target_pixels:
      neighbors = get_all_neighbors(input_grid, row, col)
      for nr, nc in neighbors:
          output_grid[nr, nc] = 8  # Change to azure

    return output_grid
```

