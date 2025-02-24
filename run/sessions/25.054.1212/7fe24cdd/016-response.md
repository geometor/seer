# 7fe24cdd • 016 • refine_coder

---
```python
"""
The transformation rule is an expansion where each cell in the 3x3 input grid maps to a 2x2 block in the 6x6 output grid.  The values within each 2x2 block are determined by the input cell and its immediate neighbors (right, below, and diagonally down-right), with zero-padding used for edge cases. The overall pattern has a pinwheel appearance.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((2 * rows, 2 * cols), dtype=int)

    for row in range(rows):
        for col in range(cols):
            # Top-left of the 2x2 block: Value of the input cell.
            output_grid[2*row][2*col] = input_grid[row][col]

            # Top-right of the 2x2 block: Value of the right neighbor (or 0 if at the right edge).
            if col + 1 < cols:
                output_grid[2*row][2*col + 1] = input_grid[row][col+1]
            else:
                output_grid[2*row][2*col + 1] = 0

            # Bottom-left of the 2x2 block: Value of the bottom neighbor (or 0 if at the bottom edge).
            if row + 1 < rows:
                output_grid[2*row + 1][2*col] = input_grid[row+1][col]
            else:
                output_grid[2*row + 1][2*col] = 0

            # Bottom-right of the 2x2 block: Value from diagonal element, handling each edge condition.
            if row + 1 < rows and col + 1 < cols:
               output_grid[2*row+1][2*col+1] = input_grid[row+1][col+1]
            # cases where original cell is on an edge
            elif row + 1 == rows and col+1 < cols:
                output_grid[2*row + 1][2 * col + 1] = input_grid[row][col+1] # bottom edge
            elif col + 1 == cols and row+1 < rows:
                output_grid[2*row + 1][2 * col + 1] = input_grid[row+1][col] # right edge
            else:
                output_grid[2*row + 1][2*col+1] = input_grid[row][col] # bottom-right corner


    return output_grid.tolist()
```
