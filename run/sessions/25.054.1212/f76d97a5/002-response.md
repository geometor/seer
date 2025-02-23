# f76d97a5 • 002 • example_1 • investigate_coder

---
```python
"""
Iterate through each cell of the input grid. If the cell value is 5 (gray), replace it with 4 (yellow). If the cell value is 4 (yellow), replace it with 0 (white).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid to preserve dimensions
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the output grid using nested loops
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the transformation rules:
            if output_grid[i, j] == 5:  # If the cell value is 5
                output_grid[i, j] = 4  # Replace it with 4
            elif output_grid[i, j] == 4:  # If the cell value is 4
                output_grid[i, j] = 0  # Replace it with 0

    return output_grid
```
