"""
The program takes a 3x3 input grid and creates a 3x3 output grid. The main diagonal (top-left to bottom-right) of the output grid is set to gray (5), while all other cells in the output grid are set to white (0). The content of the input grid doesn't affect the output grid, only the dimensions matter, in which they are the same.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input to get same dimensions
    output_grid = np.zeros_like(input_grid)
    
    # iterate through the grid and set diagonal elements to 5 (gray)
    for i in range(min(output_grid.shape)):
        output_grid[i, i] = 5

    return output_grid