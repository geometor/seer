"""
The output grid is a 9x9 grid. The program takes the 3x3 input grid and places it in the top-right corner of the output grid. The rest of the output grid is filled with zeros based on a specific interleaving pattern.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((9, 9), dtype=int)

    # get input grid dimensions
    input_height, input_width = input_grid.shape

    # Place the input grid in the top-right corner of the output grid.
    output_grid[0:input_height, 6:9] = input_grid
    
    #Top Left
    output_grid[0:input_height,0:3] = input_grid
    output_grid[0:3, 3:6]=0
    
    #Middle section
    output_grid[3:6, 0:3]=0
    output_grid[3:6, 3:6]=0
    output_grid[3:6, 6:9]=0
    
    #Bottom section
    output_grid[6:9, 0:3] = input_grid
    output_grid[6:9, 3:6]=0
    output_grid[6:9, 6:9]=0

    return output_grid