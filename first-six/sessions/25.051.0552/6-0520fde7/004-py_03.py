"""
The transformation rule involves creating a new 3x3 grid. In this new grid only color 5, mapped to color 2, is copied. Other colors are transformed to the background color.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 3x3 array filled with 0 (white)
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the positions of color 5 in the input grid
    positions_5 = np.argwhere(input_grid == 5)

    # Find min and max row and col to map the positions to the output grid
    if positions_5.size > 0:
        min_row = np.min(positions_5[:, 0])
        min_col = np.min(positions_5[:, 1])
        
        # Copy and map color 5 to color 2 in the output grid, adjusting for position
        for pos in positions_5:
            row = pos[0] - min_row
            col = pos[1] - min_col
            if 0 <= row < 3 and 0 <= col < 3:
               output_grid[row, col] = 2

    return output_grid