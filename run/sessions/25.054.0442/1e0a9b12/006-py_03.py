"""
1.  **Initialization:** Create an output grid of the same size as the input grid, filled entirely with zeros.
2.  **Row-by-Row Processing:** Iterate through the input grid row by row.
3.  **Collect Non-Zero Elements:** For each row:
    *   Collect all non-zero elements, *preserving their original order within that row*.
4.  **Placement in Output:**
    *   Start at the *last* row of the output grid.
    *   Place the collected elements from the current input row, from left to right, into the current output row.
    *   If the current output row is full, move to the row *above* and continue placing elements from left to right.
5.  **Iteration:** Repeat steps 3 and 4 for each row in the input grid.
6. **Result:** The output grid now contains all non-zero elements from the input, arranged at the bottom, preserving the original relative horizontal order *of elements within each row*. All other cells in the output are zero.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with zeros and the same shape as the input.
    output_grid = np.zeros_like(input_grid)
    rows, cols = output_grid.shape

    # Start placing non-zero elements from the last row.
    current_row = rows - 1
    current_col = 0

    # Iterate through the input grid row by row.
    for input_row in range(rows):
        # Collect non-zero elements from the current row, preserving order.
        non_zero_elements = []
        for input_col in range(cols):
            if input_grid[input_row, input_col] != 0:
                non_zero_elements.append(input_grid[input_row, input_col])

        # Place the collected elements in the output grid.
        for element in non_zero_elements:
            output_grid[current_row, current_col] = element
            current_col += 1

            # If the current output row is full, move to the next row up.
            if current_col == cols:
                current_col = 0
                current_row -= 1
                # Handle case where we run out of rows (top reached).
                if current_row < 0:
                    current_row = rows - 1 # wrap back to the bottom

    return output_grid