# 00d62c1b • 038 • refine_coder

---
```python
"""
Change green pixels to yellow if it contains a neighbor that is not green or black.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the neighbors of a cell, including diagonals"""
    rows, cols = grid.shape
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):  # Exclude the cell itself
                neighbor_row, neighbor_col = row + i, col + j
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    neighbors.append(grid[neighbor_row, neighbor_col])
    return neighbors

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is green
            if input_grid[row, col] == 3:
                # Get the neighbors of current cell
                neighbors = get_neighbors(input_grid, row, col)
                # Check if neighbors are not green and not black
                if any(neighbor != 3 and neighbor != 0 for neighbor in neighbors):
                  output_grid[row,col] = 4

    return output_grid
```
