"""
The input 5x5 grid is transformed into a 3x3 output grid. The transformation involves dividing the input grid into overlapping 3x3 regions. 
If a region contains any red (2) pixels, the corresponding center pixel in the output grid is gray (5). Otherwise, it's white (0).
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through 3x3 overlapping regions
    for i in range(3):
        for j in range(3):
            # Define the 3x3 region
            row_start = i
            row_end = i + 3
            col_start = j
            col_end = j + 3
            
            # Extract subgrid for region
            region = input_grid[row_start:row_end, col_start:col_end]

            # Check for the presence of red (2) in region and map it to gray in the output
            if 2 in region:
                output_grid[i, j] = 5  # gray
            else:
                output_grid[i,j] = 0 # white - unnecessary due to initialization

    return output_grid.tolist()