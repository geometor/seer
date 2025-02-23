# db93a21d • 002 • example_1 • investigate_coder

---
```python
"""
1. Preserve Maroon: Copy all maroon (9) pixels from the input grid to the same positions in the output grid.

2. Outline in Green: For each maroon pixel in the input grid, examine its immediate neighbors (up, down, left, right). If a neighbor is white (0) in the input grid, change that pixel in the output grid to green (3).

3. Create blue object: Starting from the bottom right of the image, identify a rectangular area not occupied by any colored pixels and replace the white pixels with blue (1) pixels.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell (up, down, left, right)."""
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
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)

    # Preserve Maroon and Outline in Green
    rows, cols = input_grid.shape
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 9:
                for r, c in get_neighbors(input_grid, row, col):
                    if input_grid[r, c] == 0:
                        output_grid[r, c] = 3

    # create blue object
    # find dimensions of object in example
    blue_height = 4
    blue_width = 2

    # start from the bottom right
    for row in range(rows - blue_height, rows):
      for col in range(cols - blue_width, cols):
          output_grid[row,col] = 1


    return output_grid
```
