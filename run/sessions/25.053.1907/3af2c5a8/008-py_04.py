"""
The transformation rule is to double the input grid, and reflect on both axis.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by doubling its dimensions and mirroring its content.
    """
    # Get input grid dimensions
    rows, cols = input_grid.shape

    # Double dimensions for output grid
    output_grid = np.zeros((rows * 2, cols * 2), dtype=int)

    # Copy the original input grid to output grid, this the top-left corner of output.
    output_grid[:rows, :cols] = input_grid
    
    # Mirror the input grid horizontally, to top-right corner of output.
    output_grid[:rows, cols:] = np.fliplr(input_grid)

    # Mirror the top part of output grid (which combines original and horizontal mirror) vertically.
    output_grid[rows:, :] = np.flipud(output_grid[:rows, :])

    return output_grid