"""
1.  **Iterate by Columns:** The transformation operates column by column.
2.  **Find Topmost Non-Zero Pixel:** For each column, find the *topmost* pixel that is not 0 (white).
3.  **Preserve First Row.** For each column, copy the value of that column in
    the first row (row 0) from the input grid to the output grid.
4.  **Create Vertical Line (Conditional):** If a non-zero pixel was found in step 2:
    *   **Base Color:** Use the color of the topmost non-zero pixel as the "base color."
    *   **Alternating Pattern:** Create a vertical line in that column, starting from the *second* row (row 1).
    *   **Odd Rows:** Fill cells in odd-numbered rows (1, 3, 5...) with the "base color."
    *   **Even Rows:** Fill cells in even-numbered rows (2, 4, 6...) with 0 (white).
5. **Skip Columns with only white:** If a column has only color white (0) then
   the column in the output will be identical.
"""

import numpy as np

def find_topmost_nonzero(grid, col):
    """Finds the topmost non-zero pixel's row index and color in a column."""
    rows = grid.shape[0]
    for r in range(rows):
        if grid[r, col] != 0:
            return r, grid[r, col]  # Return row index and color
    return None, None  # Return None if no non-zero pixel found


def transform(input_grid):
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each column (Step 1)
    for c in range(cols):
        # Find the topmost non-zero pixel (Step 2)
        top_row, top_color = find_topmost_nonzero(input_grid, c)

        #preserve value of first row from input (Step 3)
        output_grid[0,c] = input_grid[0,c]

        # Create vertical line if a non-zero pixel was found (Step 4)
        if top_color is not None:
            # Start alternating pattern from the second row (row 1)
            for r in range(1, rows):
                if (r) % 2 != 0:  # Odd rows (Step 4 - Odd Rows)
                    output_grid[r, c] = top_color
                else:  # Even rows (Step 4 - Even Rows)
                    output_grid[r, c] = 0
    # Step 5 is implicitly handled since we copy input to output.
    return output_grid