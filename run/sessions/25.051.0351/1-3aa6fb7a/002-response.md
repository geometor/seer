# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The azure (8) objects in the input grid remain unchanged. For each azure object, examine the cell directly to its right. If the cell is background color (white/0), change it to blue (1). Otherwise, leave it unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule: Azure objects remain unchanged.
    For each azure object, the cell to its right turns blue if it was white.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid
    rows, cols = input_grid.shape

    # Iterate through the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is azure (8)
            if input_grid[r, c] == 8:
                # Check if there's a cell to the right
                if c + 1 < cols:
                    # Check if the cell to the right is white (0)
                    if input_grid[r, c + 1] == 0:
                        # Change the cell to the right to blue (1)
                        output_grid[r, c + 1] = 1

    return output_grid
```

