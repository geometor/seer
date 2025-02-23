"""
1. **Expand Grid:** Double the dimensions of the input grid to create the output grid.
2. **Replicate Pixels:** For *each* pixel in the input grid, create a 2x2 block of the *same* color in the output grid. The top-left cell of this 2x2 block corresponds to the position of the original pixel multiplied by two. In other words: Every element at input_grid[row, col] becomes a 2x2 block at output_grid[row*2:row*2+2, col*2:col*2+2].
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
            color = input_grid[row, col]
            output_grid[row*2:row*2+2, col*2:col*2+2] = color
    
    return output_grid