# db93a21d • 004 • refine_coder

---
```python
"""
1. Preserve Maroon: Copy all maroon (9) pixels from the input to the output grid.
2. Green Outline:
    *   Any white (0) pixel that is adjacent (up, down, left, or right) to a maroon (9) pixel is changed to green (3) in the output.
    *   Any white pixel that is adjacent to the edge of the grid is changed to green (3) in the output
3.  Blue Object: Identify the spaces created enclosed by a green outline. Fill this shape with blue (1) pixels.
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
    rows, cols = input_grid.shape

    # Preserve Maroon
    # (No change needed here - already correct)

   # Green Outline (including edge)
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 9:  #Maroon
                for r, c in get_neighbors(input_grid, row, col):
                    if input_grid[r,c] == 0:
                        output_grid[r,c] = 3
            elif input_grid[row,col] == 0:
                is_edge = row == 0 or row == rows -1 or col == 0 or col == cols - 1
                if is_edge:
                    output_grid[row,col] = 3

    # Flood fill for blue objects
    for row in range(rows):
        for col in range(cols):
            if output_grid[row, col] == 0:
                output_grid[row,col] = 1

    return output_grid
```
