"""
Divides the input grid into 2x2 subgrids, and replaces each subgrid with a single pixel in the output grid. 
If a 2x2 subgrid in the input contains the value 7 (orange), it's replaced by 3 (green) in the output grid. Otherwise
the subgrids are discarded
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    input_rows, input_cols = input_grid.shape
    output_rows, output_cols = input_rows // 2, input_cols // 2
    output_grid = np.zeros((output_rows, output_cols), dtype=int)
    
    # Iterate through 2x2 subgrids
    for i in range(0, input_rows - input_rows%2, 2):
        for j in range(0, input_cols - input_cols%2, 2):
            subgrid = input_grid[i:i+2, j:j+2]
            # Check if the subgrid contains 7.
            if 7 in subgrid:
                output_grid[i//2, j//2] = 3
            
    return output_grid.tolist()