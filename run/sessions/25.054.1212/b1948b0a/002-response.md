# b1948b0a • 002 • example_1 • investigate_coder

---
```python
"""
Replace all magenta pixels with red pixels, leave orange pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid to preserve dimensions
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the grid
    for row_index, row in enumerate(input_grid):
        for col_index, pixel in enumerate(row):
            # change output pixels 
            # Check if the pixel is magenta (6)
            if pixel == 6:
                # Replace magenta (6) with red (2)
                output_grid[row_index][col_index] = 2
            # Orange (7) remains unchanged.

    return output_grid
```
