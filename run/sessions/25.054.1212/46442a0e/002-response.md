# 46442a0e • 002 • example_1 • investigate_coder

---
```python
"""
Replicate a 2x2 input grid to create a 4x4 output grid, maintaining the checkerboard pattern.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 4x4 array filled with zeros.
    output_grid = np.zeros((4, 4), dtype=int)

    # Fill the output grid by replicating the input grid.
    # Iterate through each cell of the output grid.
    for i in range(4):
        for j in range(4):
            # Map the output grid indices to input grid indices using modulo.
            input_row = i % 2
            input_col = j % 2
            output_grid[i, j] = input_grid[input_row, input_col]

    return output_grid
```
