"""
The output grid is constructed by making a copy of the input and adding it to the bottom. Then, the input grid is transposed and added to the right of the original.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_np = np.array(input_grid)
    rows, cols = input_np.shape
    output_grid = np.zeros((rows * 2, cols), dtype=int)

    # Duplicate and stack the input grid vertically.
    output_grid[:rows, :] = input_np
    output_grid[rows:, :] = input_np
    
    return output_grid.tolist()