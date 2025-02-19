# 1e32b0e9 • 006 • example_3 - CODE

---
```python
"""
Transformation rule:
1. Preserve all instances of color 1 (blue).
2. If any cell that is of color 3 has adjacent zeros, change those zeros to 1.
3. If any cell of color 3 has an adjacent cell of color 1, change the 3 to a 1.

"""

import numpy as np

def get_neighbors(grid, row, col):
    """Returns the valid neighbors (up, down, left, right) of a cell."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid
    for row in range(rows):
        for col in range(cols):
            if input_grid[row,col] == 3:
                for neighbor_row, neighbor_col in get_neighbors(input_grid, row, col):
                    if input_grid[neighbor_row,neighbor_col] == 0:
                         output_grid[neighbor_row,neighbor_col] = 1
    
    for row in range(rows):
        for col in range(cols):
            if input_grid[row,col] == 3:
                for neighbor_row, neighbor_col in get_neighbors(input_grid, row, col):
                    if output_grid[neighbor_row,neighbor_col] == 1:
                         output_grid[row,col] = 1
    return output_grid
```

