"""
1.  Identify the yellow pixel (value 4) in the top-left corner ([0,0]) of the input grid.
2.  Copy the yellow pixel to the cells directly below it in the first column ([1,0] and [2,0]).
3.  Identify the red pixel (value 2) in the center of the grid ([1,1]).
4.  Copy the red pixel in the cell directly below ([2,1]).
5.  Keep the all the other pixels in the input grid (those with the value of 0) in same positions.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input_grid

    # Find the yellow pixel (4) at [0, 0]
    yellow_pixel = input_grid[0, 0]
    if yellow_pixel == 4:
        # Duplicate yellow pixel vertically
       output_grid[1, 0] = yellow_pixel
       output_grid[2, 0] = yellow_pixel

    # Find the red pixel (2) at the center [1, 1]
    red_pixel = input_grid[1, 1]
    if red_pixel == 2:
        #Duplicate red pixel in the cell below.
        output_grid[2,1] = red_pixel

    return output_grid