"""
1.  **Analyze Input Rows:** Examine each row of the input grid.
2.  **Count White:** Count the number of rows that contain at least one white (0) pixel.
3.  **Assign Output Colors:** Create a 3x3 output grid. Assign colors to the output cells based on these rules
    *   If three rows contain the color 0, fill the output grid as color 2
    *   If one row contain the color 0, fill the output grid as color 4.
    *   If two rows contain the color 0, fill the output grid as color 3.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid to output based on a count of the number
    of rows containing the color white(0).
    """
    # Analyze Input Rows and Count White
    rows_with_white = 0
    for row in input_grid:
        if 0 in row:
            rows_with_white += 1

    # Create a 3x3 output grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Assign Output Colors based on the count.
    if rows_with_white == 1:
      output_grid[:] = 4
    elif rows_with_white == 2:
      output_grid[:] = 3
    elif rows_with_white == 3:
      output_grid[:] = 2
    #no else - zero case does not exist in this task

    return output_grid