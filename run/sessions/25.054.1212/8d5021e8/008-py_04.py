"""
The input grid is expanded into a larger grid. The height is tripled (3 -> 9), and the width is doubled (2 -> 4). 
The first column of the input becomes the second and forth column of the output grid. 
The second column from input is mirrowed in columns 1 and 3.
The pattern is repeated three times vertically.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with tripled height and doubled width
    output_height = input_grid.shape[0] * 3
    output_width = input_grid.shape[1] * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Mirror horizontally and vertically
    for i in range(3):  # Repeat the pattern three times vertically
        # Copy the input columns to the output, mirrored
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 1] = input_grid[:, 0]
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 2] = input_grid[:, 1]
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 0] = input_grid[:, 1]
        output_grid[i * input_grid.shape[0]:(i + 1) * input_grid.shape[0], 3] = input_grid[:, 0]

    return output_grid