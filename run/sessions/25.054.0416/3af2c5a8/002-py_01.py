"""
The transformation rule is as follows:
1. Identify all azure (8) pixels in the input grid.
2. Duplicate the input grid, effectively increasing the dimensions 2x.
3. Place the original input grid into coordinate 0,0 of the output.
4. Place the input grid at output coordinate 0,4.
5. Place the input grid at output coordinate 3,0.
6. Place the input grid at output coordinate 3,4.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)
    
    # place copies of the original grid
    output_grid[0:input_height, 0:input_width] = input_grid
    output_grid[0:input_height, input_width:output_width] = input_grid
    output_grid[input_height:output_height, 0:input_width] = input_grid
    output_grid[input_height:output_height, input_width:output_width] = input_grid

    return output_grid