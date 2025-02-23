"""
1.  **Iterate through Rows:** Examine each row of the input grid independently.
2.  **Check for Grey:** For each row, check if it contains the value 5 (grey).
3.  **Transform Row (if grey exists):** If the row contains a 5, create a new row for the output grid:
    *   Iterate through the input row.
    *   If a value in that row is 5 (grey), place a 2 (red) in the corresponding position of the output row.
    *   For all other values in the input row, place a 0 (white) in the corresponding position of the output row.
4.  **Output Grid:** Assemble the transformed rows into a 3x3 output grid. If there are fewer than three rows to transform, fill in default rows of all 0.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)
    output_row_index = 0

    # Iterate through rows of the input grid
    for i in range(input_grid.shape[0]):
        row = input_grid[i, :]

        # Check if the row contains grey (5)
        if 5 in row:
            # Create a new row for the output grid
            new_row = np.zeros(3, dtype=int) # ensure new_row is size 3

            # Iterate through input row to do transformations, limit to 3 columns.
            for j in range(min(input_grid.shape[1],3)):
                 if row[j] == 5:
                    new_row[j] = 2  # Grey to Red
                 else:
                    new_row[j] = 0  # other to white

            # add to output, using separate counter
            output_grid[output_row_index, :] = new_row
            output_row_index += 1

        # stop after 3 rows
        if output_row_index >= 3:
            break

    return output_grid