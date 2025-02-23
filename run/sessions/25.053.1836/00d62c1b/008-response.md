# 00d62c1b • 008 • example_2 - CODE

---
```python
"""
Identify yellow (4) pixels. For each yellow pixel, check its immediate neighbors (up, down, left, right). If a neighbor is green (3), move the green to be a yellow.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Returns a list of valid neighbors for a given cell in the grid.
    """
    rows, cols = grid.shape
    neighbors = []
    # Check up, down, left, right
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
    """
    Transforms the input grid according to the rule: Green pixels next to yellow pixel. Then yellow becomes green.
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find yellow cells
    yellow_pixels = []
    for r in range(rows):
      for c in range(cols):
        if output_grid[r,c] == 4:
          yellow_pixels.append((r,c))

    # change yellow to green
    for r, c in yellow_pixels:
      output_grid[r,c] = 3

    return output_grid
```
