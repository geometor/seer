# f76d97a5 • 004 • refine_coder

---
```python
"""
Iterate through each row (line) of the input grid.
For the first group of contiguous pixels of color 5 (gray) on a line:
    transform the first pixel of color 5 to color 4 (yellow).
    All other pixels of color 5 remain color 5.
All other colors are unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Iterate through each row of the grid
    for i in range(output_grid.shape[0]):
        first_five_found = False
        contiguous_block = False

        #Iterate through each cell in the row
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 5:  # Check if the cell is gray (5)
                if not first_five_found:
                    if not contiguous_block: # start a new contig block
                        output_grid[i,j] = 4 # set first 5 to 4
                        first_five_found = True
                    contiguous_block = True
                # else leave it alone

            else: # not a 5
                contiguous_block = False # reset contig block

    return output_grid
```
