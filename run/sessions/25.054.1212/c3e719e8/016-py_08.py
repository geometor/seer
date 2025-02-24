"""
The input grid is replicated four times within the output grid, at the corners of the output grid. The central 3x3 area and areas around the replicated grids, are padded with zeros (white).
"""

import numpy as np

def transform(input_grid):
    # Initialize a 9x9 output grid filled with zeros.
    output_grid = np.zeros((9, 9), dtype=int)

    # Get the dimensions of the input grid.
    input_height, input_width = input_grid.shape

    # Replicate the input grid at the top-left corner.
    output_grid[0:input_height, 0:input_width] = input_grid

    # Replicate the input grid at the top-right corner.
    output_grid[0:input_height, 9-input_width:9] = input_grid
    
    # Replicate the input grid at the bottom-left corner.
    output_grid[9-input_height:9, 0:input_width] = input_grid

    # Replicate the input grid at the bottom-right corner.
    output_grid[9-input_height:9, 9-input_width:9] = input_grid

    return output_grid