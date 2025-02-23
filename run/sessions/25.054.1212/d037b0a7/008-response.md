# d037b0a7 • 008 • example_2 • investigate_coder

---
```python
"""
replace any 0 by value to its left or right.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell of the grid.
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is 0 (white).
            if output_grid[i, j] == 0:
                # Check the cell to the right
                if j + 1 < cols:
                    if output_grid[i,j+1] !=0:
                        output_grid[i,j] = output_grid[i,j+1]
                        continue

                # Check the cell to the left,
                if j - 1 >= 0:
                     if output_grid[i,j-1] !=0:
                        output_grid[i,j] = output_grid[i,j-1]
                        continue
    return output_grid
```
