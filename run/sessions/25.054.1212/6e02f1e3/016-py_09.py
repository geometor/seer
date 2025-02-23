"""
The output grid has the same dimensions as the input grid. Gray pixels are placed
along the main diagonal (where row index equals column index). All other pixels
are white.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy to avoid modifying the original
    output_grid = np.copy(input_grid)
    
    # get dimensions
    rows, cols = output_grid.shape

    # iterate through each cell of the output grid
    for i in range(rows):
        for j in range(cols):
            # if the cell is on the main diagonal, set it to gray (5)
            if i == j:
                output_grid[i, j] = 5
            # otherwise, set it to white (0)
            else:
                output_grid[i, j] = 0

    return output_grid