# dae9d2b5 • 024 • refine_coder

---
```python
"""
The transformation takes the left half of the input grid and replaces all non-white colors with magenta, resulting in a grid with half the width of the original. White pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols // 2), dtype=int)

    # change output pixels 
    for i in range(rows):
        for j in range(cols // 2):
            if input_grid[i][j] != 0:  # Check if the pixel is not white
                output_grid[i][j] = 6  # Replace with magenta
            else:
                output_grid[i][j] = input_grid[i][j]  # Keep white pixels as they are

    return output_grid
```
