# d13f3404 • 006 • refine_coder

---
```python
"""
Each pixel in the input grid expands to a 2x2 block of the same color in the output grid. The top-left corner of each 2x2 block corresponds to the position of the original pixel in the input grid, scaled by a factor of 2.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the 2x2 block expansion rule.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros((6, 6), dtype=int)  # Initialize output grid with zeros

    # Iterate through the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Calculate the starting position in the output grid (2x scaling)
            start_row = i * 2
            start_col = j * 2

            # Fill the 2x2 block in the output grid
            output_grid[start_row:start_row+2, start_col:start_col+2] = input_grid[i, j]

    return output_grid.tolist()
```

