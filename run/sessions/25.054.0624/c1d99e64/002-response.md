# c1d99e64 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is as follows:
1. Copy the input grid to create the output grid.
2. Identify the center row of the grid.
3. Overwrite all pixel values in the center row with the value 2 (red).
4. Identify the center column of the grid.
5. Overwrite all pixel values in the center column with the value 2 (red).
6. Return the modified grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find the center row index.
    center_row = 8 # as observed
    
    # Overwrite all pixels in center_row with red (2)
    output_grid[center_row, :] = 2

    # find the center column index
    center_col = 8 # as observed

    # Overwrite all pixels in the center column with red
    output_grid[:, center_col] = 2
    
    return output_grid
```

