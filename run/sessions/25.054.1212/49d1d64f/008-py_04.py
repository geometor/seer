"""
Embeds the input grid within a larger output grid, duplicates the bordering rows and columns of the input grid, and adds 0-value padding at the corners.
"""

import numpy as np

def transform(input_grid):
    # Get dimensions of the input grid.
    input_height, input_width = input_grid.shape

    # Create a new output grid that is larger than the input grid (2 rows/cols larger).
    output_height = input_height + 2
    output_width = input_width + 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Embed the input grid into the center of the output grid.
    output_grid[1:output_height-1, 1:output_width-1] = input_grid

    # Duplicate Top Row
    output_grid[0, 1:output_width-1] = input_grid[0, :]

    # Duplicate Bottom Row
    output_grid[output_height-1, 1:output_width-1] = input_grid[-1, :]
    
    # Duplicate Left Column
    output_grid[1:output_height-1, 0] = input_grid[:, 0]

    # Duplicate Right Column
    output_grid[1:output_height-1, output_width-1] = input_grid[:, -1]
    
    # corner padding already exists as initialized

    return output_grid