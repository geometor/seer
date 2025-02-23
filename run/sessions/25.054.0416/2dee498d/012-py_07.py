"""
1. The output grid has the same height as the input grid.
2. The output grid's width is one-third the width of the input grid.
3. For each row in the input grid, take the pixel values from the columns at indices 0, 3, 6, 9, and so on.
4. Place these selected pixel values sequentially into the columns of the output grid, starting from column 0. In other words, the *i*-th selected column from the input becomes the *i*-th column in the output.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height
    output_width = input_width // 3
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Change output pixels
    for j in range(output_width):
        # Select columns from input_grid at intervals of 3
        output_grid[:, j] = input_grid[:, j * 3]

    return output_grid