"""
1.  **Determine Output Dimensions:** The output grid's height is determined based on how many rows containing a '1' value are present. That number of rows containing '1' + 2. Each row contains 1 value of '1'. The output grid's width is the same as the input's width.

2.  **Iterate through Input Grid:** For each column in the input grid, create a column of the output grid by duplicating the value the number of times as the number of rows.

3.  **Populate Output:**
    *   Iterate through each column from the input grid.
    *   For input grid columns: Create an output column where: The cells from top to bottom will contain a number from left to right of the input grid, and the rest will be filled with "0".
    *   Example input column `[2, 3, 1]` becomes output column `[1, 2, 3, 0, 0]`

In summary the transformation stacks the values from the input column into output column, and completes with white cells.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows_with_1 = np.count_nonzero(input_grid == 1)
    output_height =  input_grid.shape[0] + 2
    output_width = input_grid.shape[1]
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for j in range(input_grid.shape[1]):
        # Get the values from the input column
        input_column_values = input_grid[:, j]

        # Rotate the values to match the order requested
        rotated_values = np.roll(input_column_values, -np.argmax(input_column_values == 1))

        # Place the rotated values at the beginning of output_grid
        output_grid[:input_grid.shape[0],j] = rotated_values


    return output_grid.tolist()