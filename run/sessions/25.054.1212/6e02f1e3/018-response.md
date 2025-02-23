# 6e02f1e3 • 018 • refine_coder

---
```python
"""
The output grid has the same dimensions as the input grid. The color of pixels
on the main diagonal (where row index equals column index) are set to grey (5)
if the row index is 0, and 5 if all the values of the grid are the same.
Otherwise, the diagonal pixels match the input's values. Pixels not on the main
diagonal remain unchanged from the input grid to the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy to avoid modifying the original
    output_grid = np.copy(input_grid)
    
    # get dimensions
    rows, cols = output_grid.shape

    # check if all values in the grid are the same
    first_value = input_grid[0, 0]
    all_same = np.all(input_grid == first_value)

    # iterate through each cell of the output grid
    for i in range(rows):
        for j in range(cols):
            # if the cell is on the main diagonal
            if i == j:
                # if it's the first row or all values are the same, set to gray
                if i == 0 or all_same:
                    output_grid[i, j] = 5
                # otherwise, keep the original value (already copied)
            # else:  # Not on the diagonal
                # output_grid[i, j] = input_grid[i,j] #- keep input, already done

    return output_grid
```
