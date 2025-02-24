"""
The input grid (5x5) is transformed into a smaller output grid (3x3). 
Green pixels in specific regions of the input grid determine the presence of gray pixels in the output grid.
If there is at least one green pixel in the top-right 3x3 region of input, the top right of output is gray.
If there is at least one green pixel in the bottom-left 3x3 region of input, the bottom left of output is gray.
All other output pixels default to white.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as 3x3 with all white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Check top-right 3x3 region of input_grid
    top_right_region = input_grid[0:3, 2:5]
    if np.any(top_right_region == 3):
        output_grid[0:1, 2:3] = 5  # Set top-right corner of output to gray

    # Check bottom-left 3x3 region of input
    bottom_left_region = input_grid[2:5, 0:3]
    if np.any(bottom_left_region == 3):
         output_grid[2:3, 0:3] = 5 # set bottom row to grey
    
    return output_grid