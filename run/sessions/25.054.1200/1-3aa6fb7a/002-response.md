# 1-3aa6fb7a • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify**: Locate all azure pixels (value 8) in the input grid.
2.  **Check Adjacency and Insert**: For each azure pixel moving from west to east across the grid, and if the azure pixel does not have a azure neighbor to its right, create a blue pixel on the east edge.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # change output pixels 
    for r in range(rows):
        for c in range(cols):
            #Find Azure
            if input_grid[r, c] == 8:
                #check east neighbor, skip if on the edge
                if c + 1 < cols:
                    if input_grid[r, c + 1] != 8:
                       output_grid[r,c+1] = 1

    return output_grid
```
