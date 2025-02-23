# 25d8a9c8 • 020 • example_4 • investigate_coder

---
```python
"""
Examine each pixel in the input grid.
If the pixel's value is 1 (blue), change it to 5 (gray) in the output grid.
Otherwise, change the pixel's value to 0 (white) in the output grid.
Return the changed grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # iterate over each cell of the grid and perform the transformation
    for row_index, row in enumerate(input_grid):
      for col_index, pixel in enumerate(row):
        # If the pixel's value is 1 (blue), change it to 5 (gray)
        if pixel == 1:
          output_grid[row_index,col_index] = 5
        # Otherwise, change the pixel's value to 0 (white).
        else:
          output_grid[row_index,col_index] = 0
    return output_grid
```
