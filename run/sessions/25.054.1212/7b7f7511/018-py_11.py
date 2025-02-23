"""
The program transforms the input grid into the output grid by cropping it to its left half.

1.  **Determine Input Dimensions:** Get the number of rows and columns of the input grid.
2.  **Calculate Output Columns**: Calculate the number of columns in the output. This is exactly half the number of columns in the input, rounding down.
3. **Calculate Output Rows:** Calculate the number of output rows. This is always equal to the number of input rows, except when the input is square, in which case it is half of the input rows.
4.  **Crop Grid:** Create the output grid by keeping all of the rows and by keeping the columns from the left (index 0) of the input grid up to, but not including, the calculated output columns.
5.  **Output:** The output is always the left half of the input.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_rows = len(input_grid)
    input_cols = len(input_grid[0])
    output_cols = input_cols // 2
    if input_rows == input_cols:
        output_rows = input_rows // 2
    else:
        output_rows = input_rows
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # change output pixels
    for i in range(output_rows):
        for j in range(output_cols):
            output_grid[i][j] = input_grid[i][j]

    return output_grid