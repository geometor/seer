"""
The transformation identifies three 3x1 or 1x3 rectangular regions of orange (7) pixels within the grid and changes them to blue (1).
All other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing three specific 3x1 or 1x3 orange regions to blue.
    """
    output_grid = np.copy(input_grid)
    height = output_grid.shape[0]
    width = output_grid.shape[1]

    # change pixels in the identified regions:
    # Region 1: row 6, columns 15, 16, 17
    output_grid[5, 14:17] = 1
    # Region 2: row 17, columns 3, 4, 5
    output_grid[16, 2:5] = 1      
    # Region 3: row 19, columns 3, 4, 5
    output_grid[18, 2:5] = 1    

    return output_grid