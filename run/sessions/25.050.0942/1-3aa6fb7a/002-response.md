# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
Find azure (8) cells that are not horizontally or vertically connected to another azure cell. 
Then, change the color of that cell from azure (8) to blue (1). 
Azure cells which have horizontal/vertical azure neighbors must remain azure.
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

