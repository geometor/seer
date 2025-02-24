# 794b24be • 050 • example_9 • investigate_coder

---
```python
"""
Replaces all occurrences of '1' (blue) with '2' (red) in the input grid, while leaving '0' (white) unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input.
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # If the cell's value is 1, change it to 2 in the output grid.
            if output_grid[i, j] == 1:
                output_grid[i, j] = 2
            # Otherwise (if the cell's value is 0), leave it unchanged.  The copy operation already handles this.

    return output_grid
```
