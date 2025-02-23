"""
1.  **Identify the Blue Line:** Locate the vertical column in the input grid where all pixels are blue (color value 1). Note its column index.
2.  **Create Output Grid:** Generate an output grid with the same height as the input grid but with a fixed width of 3. Initially, fill the entire output grid with white pixels (color value 0).
3.  **Apply Azure Pattern:** Iterate through the rows of the output grid, applying the following rules to place azure (color value 8) pixels:

    *   **Rows above and including row index of 2:**
        * if row index 0, then position can be [0,8,0]
        * if row index 1, then position can be [0,0,8]
        * if row index 2, then position can be [0,8,8]
    *   **Row Index > 2:**
        * if the row above is all zeros and current row index is even, then [0,8,0] or [0,8,8]
        * if the row above is all zeros and current row index is odd, then [0,8,8]
        * if the row above has any azure and the current row index is even, then all zero
        * if the row above has any azure and the current row is odd:
           - if row above is [0,8,0], current row is [0,8,8]
           - if row above is [0,8,8], current row is [8,0,8]
           - if row above is [0,0,8], current row is [8,0,0]

4. **Complete:** The resulting output grid is the transformed output.
"""

import numpy as np

def find_blue_line(grid):
    """Finds the column index of the vertical blue line."""
    rows, cols = grid.shape
    for j in range(cols):
        if np.all(grid[:, j] == 1):
            return j
    return -1

def apply_azure_pattern(output_grid, row_index):
    """Applies the azure pattern to the output grid based on row index and previous row."""
    rows, cols = output_grid.shape

    if row_index == 0:
        output_grid[row_index, 1] = 8
    elif row_index == 1:
        output_grid[row_index, 2] = 8
    elif row_index == 2:
        output_grid[row_index, 1:3] = 8
    else:
        prev_row = output_grid[row_index - 1]
        if np.all(prev_row == 0):
            if row_index % 2 == 0:
                # Check surrounding rows for azure pattern to guess between [0,8,0] and [0,8,8]
                if row_index > 3 and np.array_equal(output_grid[row_index-3],[8,0,0]):
                    output_grid[row_index, 1] = 8
                else:
                    output_grid[row_index, 1:3] = 8  # Default to [0,8,8]
            else:
                output_grid[row_index, 1:3] = 8
        else:
            if row_index % 2 == 0:
                output_grid[row_index] = 0
            else:
                if np.array_equal(prev_row, [0, 8, 0]):
                    output_grid[row_index, 1:3] = 8
                elif np.array_equal(prev_row, [0, 8, 8]):
                    output_grid[row_index, 0] = 8
                    output_grid[row_index, 2] = 8
                elif np.array_equal(prev_row, [0, 0, 8]):
                    output_grid[row_index, 0] = 8


def transform(input_grid):
    # initialize output_grid
    rows, _ = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    # Find the blue line (not used for direct placement, but might be useful later)
    _ = find_blue_line(input_grid)

    # Apply azure pattern row by row
    for i in range(rows):
        apply_azure_pattern(output_grid, i)
        
    return output_grid