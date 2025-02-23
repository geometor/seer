# 6-0520fde7 • 006 • example_3 - CODE

---
```python
"""
The transformation focuses on the central column of the input grid.
A 3x3 output grid is created and filled with 0 (white).
If a cell in the input's central column is 5 (gray), the corresponding
row in the output grid's first column has a 2 (red).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 3x3 array filled with 0s.
    output_grid = np.zeros((3, 3), dtype=int)

    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape

    # Find the center column index of the input grid.
    center_col = cols // 2

    # Iterate through the rows of the input grid's central column.
    for i in range(min(rows, 3)):  # Limit to the size of the output grid
        # Check if the pixel in the central column is color 5 (gray).
        if input_grid[i, center_col] == 5:
            # If so, set the corresponding pixel in the output grid to color 2 (red).
            output_grid[i, 0] = 2

    return output_grid
```

