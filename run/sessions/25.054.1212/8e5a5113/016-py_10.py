"""
1. Copy Initial Columns: Copy the first four columns (index 0 to 3) of the input grid directly to the output grid (columns 0 to 3).
2. Copy Final Columns: Copy the last three columns (index 8 to 10) of the input grid directly to the output grid (columns 8 to 10).
3. Sequence Columns: Create columns 4, 5, 6 and 7 in output, using the following.
   - Column 4 is set to column 0.
   - Column 5 is set to column 1.
   - Column 6 is set to column 2.
   - Column 7 is set to column 3.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input grid
    output_grid = np.copy(input_grid)

    # Sequence Columns
    output_grid[:, 4] = input_grid[:, 0]
    output_grid[:, 5] = input_grid[:, 1]
    output_grid[:, 6] = input_grid[:, 2]
    output_grid[:, 7] = input_grid[:, 3]

    return output_grid