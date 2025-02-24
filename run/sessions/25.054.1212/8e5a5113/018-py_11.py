"""
1.  **Copy Initial Columns:** Copy the first four columns (0-3) of the input grid directly to the output grid (columns 0-3).
2.  **Reverse and Copy for Middle Columns:**
    *   Copy column 3 of the input to column 4 of the output.
    *   Copy column 2 of the input to column 5 of the output.
    *   Copy column 1 of the input to column 6 of the output.
    *   Copy column 0 of the input to column 7 of the output.
3.  **Transform Final Columns:** Copy the last three columns (8-10) of the input grid to the last three columns of the output grid. The top pixel of the last three columns of the input, becomes the bottom of the last three columns. The second from top pixel of the last three columns of the input, becomes the second from the bottom pixel of the last three columns. The third from the top pixel of the last three columns of the input becomes the top pixel of the last three columns.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input grid
    output_grid = np.copy(input_grid)

    # Copy Initial Columns (0-3)
    output_grid[:, 0:4] = input_grid[:, 0:4]

    # Reverse and Copy for Middle Columns (4-7)
    output_grid[:, 4] = input_grid[:, 3]
    output_grid[:, 5] = input_grid[:, 2]
    output_grid[:, 6] = input_grid[:, 1]
    output_grid[:, 7] = input_grid[:, 0]

    # Transform Final Columns (8-10)
    num_rows = input_grid.shape[0]
    for i in range(8, 11):
        for j in range(num_rows):
            output_grid[j, i] = input_grid[num_rows - 1 - j, i]
    return output_grid