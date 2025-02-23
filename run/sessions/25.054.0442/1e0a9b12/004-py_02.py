"""
1.  **Initialization:** Create an output grid of the same size as the input grid, filled entirely with zeros.
2. **Collection and Placement:** Iterate through the input grid row by row, and within each row, from left to right.
3.  **Non-zero Element Handling:** For each non-zero element encountered:
    *   Place the element in the output grid, starting at the *beginning* of the last row.
    *   If the last row is full, start to use positions in the row above, filling left to right.
    *   Continue filling upward in rows, maintaining the original horizontal order of elements *within each row*, and the relative vertical order of elements.
4. **Result:** The output grid now contains all non-zero elements from the input, arranged at the bottom, preserving original relative order and wrapping to the next higher row when a row is filled. All other cells in the output are zero.
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
        for input_col in range(cols):
            # If a non-zero element is found.
            if input_grid[input_row, input_col] != 0:
                # Place the element in the output grid.
                output_grid[current_row, current_col] = input_grid[input_row, input_col]
                current_col += 1

                # If the current row is full, move to the next row up.
                if current_col == cols:
                    current_col = 0
                    current_row -= 1
                    # Handle case where we run out of rows going upward (should not happen in ARC, given the test examples and the prompt's mention that output size is same as input size, but makes it more general)
                    if current_row < 0:
                        return output_grid # Or raise an exception, or whatever is appropriate

    return output_grid