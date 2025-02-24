# 794b24be • 020 • example_4 • investigate_coder

---
```python
"""
1. Preserve Zeros: Copy all cells with the value 0 (white) from the input grid to the output grid, maintaining their positions.
2. Transform Blues: If the input grid contains a cell with the value of 1 (blue), it will become 2 (red) in the output grid, and if it contains a cell with any other value, copy it from the input grid to the output grid.
3. Iterate over entire output grid, replacing 1 with 2
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Change output pixels: if the value is 1, change to 2
            if output_grid[i, j] == 1:
                output_grid[i, j] = 2

    return output_grid
```
