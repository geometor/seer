# 00d62c1b • 002 • example_1 - CODE

---
```python
"""
Identifies green (3) pixels in a grid and changes their color to yellow (4) 
if they have at least two orthogonally adjacent green neighbors.
"""

import numpy as np

def get_orthogonal_neighbors(grid, row, col):
    """Returns a list of orthogonally adjacent neighbors for a given cell."""
    neighbors = []
    rows, cols = grid.shape
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
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is green (3)
            if input_grid[row, col] == 3:
                # Get orthogonal neighbors
                neighbors = get_orthogonal_neighbors(input_grid, row, col)
                # Count green neighbors
                green_neighbors = 0
                for r, c in neighbors:
                    if input_grid[r, c] == 3:
                        green_neighbors += 1
                # Change color to yellow (4) if at least two green neighbors
                if green_neighbors >= 2:
                    output_grid[row, col] = 4

    return output_grid
```
