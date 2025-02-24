"""
Divides the input grid into 2x2 subgrids. If a 2x2 subgrid contains at least one orange (7) pixel, 
a green (3) pixel is placed in a 4x4 output grid. The position of the green pixel is determined by the 
position of the orange pixel within the input grid, as detailed in the natural language program.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 4x4 output grid with all zeros (black).
    output_grid = np.zeros((4, 4), dtype=int)
    input_grid = np.array(input_grid)
    input_rows, input_cols = input_grid.shape

    # Iterate through 2x2 subgrids.
    for i in range(0, input_rows - input_rows % 2, 2):
        for j in range(0, input_cols - input_cols % 2, 2):
            subgrid = input_grid[i:i+2, j:j+2]
            # Check if the subgrid contains orange (7).
            if 7 in subgrid:
                # Find the first orange pixel's row index
                orange_indices = np.where(subgrid == 7)
                first_orange_row = i + orange_indices[0][0]

                # Calculate output row index based on orange position.
                if (first_orange_row % 2) == 0:
                  output_row = (first_orange_row // 4) * 2
                else:
                  output_row = ((first_orange_row - 1) // 4) * 2 + 1

                # Calculate output column index.
                output_col = j // 2
                
                output_grid[output_row, output_col] = 3

    return output_grid.tolist()