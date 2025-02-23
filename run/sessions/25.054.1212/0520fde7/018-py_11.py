"""
1.  **Find Gray Stripe:** Locate the vertical column in the input grid that is entirely filled with gray pixels.
2.  **Map Input Rows to Output Rows:** Divide the input grid rows into three equal zones. Each zone corresponds to a row in the 3x3 output grid. For example, if the input has 6 rows, rows 0-1 map to output row 0, rows 2-3 map to output row 1, and rows 4-5 map to output row 2.
3. **Identify Blue Segments for Each Mapped Zone:** For each of the three row zones:
    -   Check for contiguous blue pixels immediately to the left of the gray stripe.
    -   Check for contiguous blue pixels immediately to the right of the gray stripe.
4.  **Create Output Grid:** Create a 3x3 output grid filled with white pixels.
5.  **Place Red Pixels:** For each output row (and corresponding input row zone):
    -   If there are blue pixels to the *left* of the gray stripe within the mapped input rows, place a red pixel in the leftmost column (column 0) of the output grid's current row.
    -   If there are blue pixels to the *right* of the gray stripe within the mapped input rows, place a red pixel in the rightmost column (column 2) of the output grid's current row.
    - If blue segments are present on both the left *and* right, in the same mapped input zone, place two red pixels: one at column 0 and one at column 2.
    - Only place at most 1 red pixel per side, per segment.
"""

import numpy as np

def find_vertical_stripe(grid, color):
    # Find the complete vertical stripe of a specific color.
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == color for i in range(rows)):
            return j
    return -1

def map_input_rows(input_rows):
    # map input rows to output rows
    zone_size = input_rows / 3
    row_mapping = {}
    for output_row in range(3):
        start_input_row = int(output_row * zone_size)
        end_input_row = int((output_row + 1) * zone_size)
        row_mapping[output_row] = list(range(start_input_row, end_input_row))
    return row_mapping

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)
    input_rows, input_cols = input_grid.shape

    # Find the vertical gray stripe (color 5).
    gray_stripe_col = find_vertical_stripe(input_grid, 5)

    if gray_stripe_col == -1:
        return output_grid  # No gray stripe found.

    # map input rows to output
    row_mapping = map_input_rows(input_rows)

    # Identify horizontal runs of blue (color 1) adjacent to the gray stripe.
    for output_row in range(3):
        left_found = False
        right_found = False
        for input_row in row_mapping[output_row]:
            if 0 <= gray_stripe_col - 1 < input_cols and input_grid[input_row, gray_stripe_col - 1] == 1 and not left_found :
                output_grid[output_row, 0] = 2
                left_found = True
            if 0 <= gray_stripe_col + 1 < input_cols and input_grid[input_row, gray_stripe_col + 1] == 1 and not right_found:
                output_grid[output_row, 2] = 2
                right_found = True

    return output_grid