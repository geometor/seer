# 67385a82 • 002 • example_1 • investigate_coder

---
```python
"""
Transforms a 3x3 input grid based on these rules:
1. If a cell is white (0), it remains 0.
2. If a cell is green (3) AND in the top two rows, it changes to azure (8).
3. If a cell is green (3) AND in the bottom row, it remains green (3).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid and apply the transformation rules.
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 3:  # Check if the cell is green.
                if r < 2:  # Check if in the top two rows
                    output_grid[r, c] = 8  # Change to azure.
                # If in the bottom, we leave as original value in output_grid
            # if not 3, also leave as orignal, already in place

    return output_grid
```

