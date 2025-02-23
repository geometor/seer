# 2-0ca9ddb6 • 006 • example_3 - CODE

---
```python
"""
The transformation rule is as follows:
1. The digits 1, 2, and 6 remain unchanged in their original positions.
2. The digit 4 is added to the output grid in locations that are directly above, below, left, or right of the digit '2' in the input grid, if those locations contain a '0' in the input.
3. The digit 7 is added to the output grid in locations that are directly above, below, left, or right of the digit '1' in the input grid, if those locations contain a '0' in the input.
4. All other 0's in the input grid that are not adjacent to '1' or '2' remain 0 in the output grid.
"""

import numpy as np

def get_neighbors(grid, row, col):
    # Get the neighbors (up, down, left, right) of a cell.
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
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # Iterate through the input grid
    for row in range(rows):
        for col in range(cols):
            # Condition 2: Add 4 around 2
            if input_grid[row, col] == 2:
                for neighbor_row, neighbor_col in get_neighbors(input_grid, row, col):
                    if input_grid[neighbor_row, neighbor_col] == 0:
                        output_grid[neighbor_row, neighbor_col] = 4
            # Condition 3: Add 7 around 1
            elif input_grid[row, col] == 1:
                for neighbor_row, neighbor_col in get_neighbors(input_grid, row, col):
                    if input_grid[neighbor_row, neighbor_col] == 0:
                        output_grid[neighbor_row, neighbor_col] = 7

    return output_grid
```
