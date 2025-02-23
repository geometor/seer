"""
The transformation rule is as follows:

1. **Expand the Grid:** Double the dimensions of the input grid. The number of rows in the output grid is twice the number of rows in the input grid. The number of columns in the output grid is twice the number of columns in the input grid.

2. **Replicate and shift the azure pixels:** For each azure (8) pixel in the input, create a copy and a new cell to the right.

3. Fill with 0: all other locations are now filled with a 0.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_rows, input_cols = input_grid.shape
    output_rows = input_rows * 2
    output_cols = input_cols * 2
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # change output pixels 
    for row in range(input_rows):
        for col in range(input_cols):
            if input_grid[row, col] == 8:
                output_grid[row * 2, col * 2] = 8
                output_grid[row*2, col*2 + 1] = 8
    
    return output_grid