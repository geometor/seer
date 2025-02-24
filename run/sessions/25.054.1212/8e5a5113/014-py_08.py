"""
1. Copy Initial Columns: Copy the first four columns (index 0 to 3) of the input grid directly to the output grid.
2. Copy Final Columns: Copy the last three columns (index 8 to 10) of the input grid directly to the output grid.
3. Sequence Columns: Create columns 4, 5 and 6 in output, using the following.
   - Column 4 is set to column 3.
   - Column 5 is set to column 7 reversed.
   - Column 6 is set to column 3 reversed.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input grid
    output_grid = np.copy(input_grid)

    # Copy the first four columns (0-3)
    # output_grid[:, :4] = input_grid[:, :4] # already done by copy

    # Copy the last three columns (8-10)
    # output_grid[:, 8:] = input_grid[:, 8:] # already done by copy

    # Sequence Columns
    output_grid[:, 4] = input_grid[:, 3]
    output_grid[:, 5] = input_grid[::-1, 7]
    output_grid[:, 6] = input_grid[::-1, 3]

    return output_grid