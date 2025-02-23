# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule identifies isolated azure (8) colored cells and changes their color to blue (1).
An isolated cell is one that has no adjacent neighbors of the same color (8).  Adjacency is defined as sharing an edge (horizontal or vertical), not just a corner.
All other cells, including non-isolated azure cells and cells of other colors, remain unchanged.
"""

import numpy as np

def _is_isolated(grid, row, col, color):
    """Checks if a cell at (row, col) of the given color is isolated."""
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and grid[nr, nc] == color:
            return False  # Found a neighbor of the same color
    return True

def transform(input_grid):
    """
    Transforms the input grid by changing isolated azure (8) cells to blue (1).
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input

    # Iterate through each cell in the grid
    for row in range(output_grid.shape[0]):
        for col in range(output_grid.shape[1]):
            # Check if the cell is azure (8) and isolated
            if output_grid[row, col] == 8 and _is_isolated(output_grid, row, col, 8):
                output_grid[row, col] = 1  # Change to blue (1)

    return output_grid
```

