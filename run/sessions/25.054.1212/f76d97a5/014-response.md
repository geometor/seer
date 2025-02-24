# f76d97a5 • 014 • example_3 • investigate_coder

---
```python
"""
The output grid is the same size as the input. All 5s in the input grid are replaced by 0s in the output grid. 9s in the input grid that have a 5 to their immediate right or immediate down are replaced by 0s, the rest of the 9s are kept as 9s.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid with 0s
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # iterate through input grid
    for r in range(rows):
        for c in range(cols):
            # check for 9
            if input_grid[r, c] == 9:
                # check neighbors, default to keeping the 9
                keep_9 = True
                # Check down neighbor
                if r + 1 < rows:
                  if input_grid[r+1,c] == 5:
                    keep_9 = False
                #check right neighbor
                if c + 1 < cols:
                  if input_grid[r,c+1] == 5:
                    keep_9 = False
                
                if keep_9:
                  output_grid[r,c] = 9

            #5s are already 0 in output_grid

    return output_grid
```
