# a85d4709 • 004 • refine_coder

---
```python
"""
The transformation replaces '0' (white) values in the input grid with a repeating pattern of '3' (green), '4' (yellow), and '2' (red), based on the row index.  '5' (gray) values in the input grid are copied directly to the output grid, acting as "stoppers" to the pattern. The pattern restarts for each row.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same shape as the input
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for i in range(rows):
        for j in range(cols):
            # If the input cell is '5', copy it to the output
            if input_grid[i, j] == 5:
                output_grid[i, j] = 5
            else:
                # Apply the row-based pattern
                if i == 0:
                    output_grid[i, j] = 3
                elif i == 1:
                    output_grid[i, j] = 4
                elif i == 2:
                    output_grid[i, j] = 2

    return output_grid
```
