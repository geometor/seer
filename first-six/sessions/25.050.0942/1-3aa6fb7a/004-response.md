# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation rule is the following: Check every azure (8) cell. If an azure cell does not have any horizontally or vertically adjacent azure cells, it changes its color to blue (1). All other azure cells remain the same. The overall structure and position of most azure shapes/objects are preserved except where isolated azure cells become blue.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Change isolated azure (8) cells to blue (1).
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the cell is azure (8)
            if input_grid[r, c] == 8:
                # Check neighbors (up, down, left, right)
                neighbors = []
                if r > 0:
                    neighbors.append(input_grid[r-1, c])  # Up
                if r < rows - 1:
                    neighbors.append(input_grid[r+1, c])  # Down
                if c > 0:
                    neighbors.append(input_grid[r, c-1])  # Left
                if c < cols - 1:
                    neighbors.append(input_grid[r, c+1])  # Right

                # Check if any neighbor is also azure (8)
                is_isolated = True
                for neighbor_color in neighbors:
                    if neighbor_color == 8:
                        is_isolated = False
                        break

                # If isolated, change to blue (1)
                if is_isolated:
                    output_grid[r, c] = 1

    return output_grid
```

