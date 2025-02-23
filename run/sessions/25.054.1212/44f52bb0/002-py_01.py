"""
Counts the number of red pixels (value '2') in the input grid, and outputs a 1x1 grid with a single blue pixel (value '1').
"""

import numpy as np

def transform(input_grid):
    # Count the number of red pixels (value 2).
    red_count = np.count_nonzero(input_grid == 2)

    # Create a 1x1 output grid.
    output_grid = np.zeros((1, 1), dtype=int)
    
    #Set value of output to 1.
    output_grid[0,0] = 1

    return output_grid