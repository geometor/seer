# c9e6f938 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation doubles the width of the input grid, copies the orange (7) pattern to the right,
and fills the remaining spaces with white (0) pixels.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid by doubling the width of the input grid.
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols * 2), dtype=int)

    # Iterate through each row.
    for i in range(rows):
        # Copy the original row to the output grid.
        output_grid[i, :cols] = input_grid[i]
        
        # Duplicate orange pattern
        for j in range(cols):
          if input_grid[i,j] == 7:
            output_grid[i,j+cols] = 7

    return output_grid
```
