# d23f8c26 • 002 • example_1 • investigate_coder

---
```python
"""
Keep only the pixels with values '3' and '4', and set all other pixels to '0'.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid, ensures same size and type
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell of the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Check if the current cell's value is 3 or 4
            if input_grid[i, j] == 3 or input_grid[i, j] == 4:
                # Preserve the pixel value
                output_grid[i, j] = input_grid[i, j]

    return output_grid
```
