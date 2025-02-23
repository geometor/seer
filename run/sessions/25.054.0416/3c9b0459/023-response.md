# 3c9b0459 • 023 • refine_coder

---
```python
"""
The transformation involves reflecting the grid along the main diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left) *separately*.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by reflecting it across the main diagonal and the anti-diagonal independently.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = input_grid.copy()  # Start with a copy of the input

    # Reflect across the main diagonal
    for r in range(rows):
        for c in range(cols):
            output_grid[c, r] = input_grid[r, c]

    # Reflect across the anti-diagonal
    temp_grid = output_grid.copy() # use a temporary copy to avoid overwriting
    for r in range(rows):
        for c in range(cols):
            output_grid[rows - 1 - c, cols - 1 - r] = temp_grid[r, c]


    return output_grid
```
