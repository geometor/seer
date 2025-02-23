"""
The input grid is divided into 9 equal 3x3 sections. Each section contains azure grid lines and can contain blue (1) and red (2) pixels. The output is a 3x3 grid. Each cell in the 3x3 output corresponds to the colors in the input grid.  Blue (1) and red (2) pixels are preserved, while azure (8) and white (0) are replaced with white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 3x3 array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Define the dimensions of the sub-grids.
    subgrid_height = 3
    subgrid_width = 3
    
    # Iterate through input and extract color to output grid based on location.
    for row in range(3):
        for col in range(3):
            input_row = row * subgrid_height + 1
            input_col = col * subgrid_width + 1

            input_cell_val = input_grid[input_row][input_col]

            if input_cell_val == 1 or input_cell_val == 2:
               output_grid[row][col] = input_cell_val
            elif input_cell_val == 8 or input_cell_val == 0:
                output_grid[row][col] = 0
            
    return output_grid