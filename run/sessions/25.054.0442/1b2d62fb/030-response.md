# 1b2d62fb • 030 • refine_coder

---
```python
"""
1.  **Extract:** Take the first three columns of the input grid to form the initial output grid.
2.  **Conditional Modification:** Iterate through each cell of the *original input grid* within the first three columns (columns 0, 1, and 2).
3.  **Rule Application:**
    *   If an input grid cell in the first three colums is '0' AND the corresponding cell in the *fourth* column of the *input grid* is NOT '1', then set the corresponding cell in the output grid to '8'.
    *   if an input grid cell in the first three columns is not '0', then set the corresponding cell in the output grid to 0.
4.  **Output:** The modified grid (which started as the first three columns of the input) is the final output.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the first three columns of the input
    output_grid = input_grid[:, :3].copy()

    # Iterate through the first three columns of the input_grid
    for i in range(input_grid.shape[0]):
        for j in range(3):
            # Apply the conditional rule
            if input_grid[i, j] == 0 and input_grid[i, 3] != 1:
                output_grid[i, j] = 8
            elif input_grid[i,j] != 0:
                output_grid[i,j] = 0

    return output_grid
```
