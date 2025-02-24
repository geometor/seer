# cce03e0d • 018 • refine_coder

---
```python
"""
The transformation rule involves replicating the 3x3 input grid within a 9x9 output grid according to a specific pattern, and filling the remaining cells with zeros. The input grid is placed intact into the top-right corner of the output grid. It appears again at the top-left. It is also placed in the bottom-left corner. The rest of the cells are filled based on a pattern relative to the position of these copies. The input grid is tiled horizontally in the first 3 rows and vertically every 3 columns.

1.  Create a 9x9 output grid filled with zeros.
2.  Place the 3x3 input grid into the top-right corner of the output grid (rows 0-2, columns 6-8).
3.  Place the 3x3 input grid into the top-left corner of the output grid (rows 0-2, columns 0-2).
4.  Place the 3x3 input grid into the bottom-left corner of the output grid (rows 6-8, columns 0-2).
5.  Fill in the output grid cells as follow:
    *   In the first three rows(0-2), copy the input grid into every set of three columns.
    *   In the last three rows (6-8), copy the input grid columns at intervals of 3 columns,
    *   Fill the remaining cells of output grid with 0.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((9, 9), dtype=int)

    # get input grid dimensions
    input_height, input_width = input_grid.shape

    # Place the input grid in the top-right corner of the output grid.
    output_grid[0:input_height, 6:9] = input_grid
    
    #Top Left
    output_grid[0:input_height,0:3] = input_grid
    
    #Bottom Left
    output_grid[6:9, 0:3] = input_grid

    # Top Row Replication
    output_grid[0:3, 3:6] = input_grid
    
    return output_grid
```
