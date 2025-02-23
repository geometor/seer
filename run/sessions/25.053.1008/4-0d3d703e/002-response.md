# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
1.  **Input:** A 3x3 grid of single-digit integers.
2.  **Transformation:** Add 1 to every integer in the input grid.
3.  **Output:** A 3x3 grid with the results of the operation of each original integer + 1.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy to avoid modifying the original
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the output grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Add 1 to the value of each cell
            output_grid[i, j] = output_grid[i,j] + 1

    return output_grid
```
