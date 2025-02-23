"""
1.  **Find the Longest Blue Line:** Identify the longest vertical line of blue (1) pixels in the input grid. Note its starting row, column index, and length.
2.  **Check for Adjacent Whites:** Determine if there are *any* white (0) pixels directly to the left *or* right of the *entire* blue line (not just row by row, but for the column as a whole).
3.  **Determine Output Dimensions:**
    *   **Height:** The output grid height is equal to the length of the longest blue line.
    *   **Width:**
        *   If there are *any* white pixels to the left *or* right of the blue line, the output width is 3.
        *   If there are *no* white pixels to the left *or* right of the blue line, the output width is 1.
4.  **Create Output Grid:** Create an output grid filled with black (0) pixels, with the determined height and width.
5.  **Populate with Azure:**
    *    A vertical line of Azure (8) will always exist in the center of the output grid, for all rows, with a height equal to the length of the blue line.
    *   Iterate through each row of the *input grid* that corresponds to the blue line:
      * If, in a given row, there's a white pixel to the immediate left of the blue pixel *in the input*, place an azure pixel in the first column of the corresponding row in the *output* grid.
      * If, in a given row, there's a white pixel to the immediate right of the blue pixel *in the input*, place an azure pixel in the third column of the corresponding row in the *output* grid.
6.  **Return:** Return the resulting output grid.
"""

import numpy as np

def find_vertical_line(grid, value):
    """Finds the longest vertical line of a specific value in a grid."""
    rows, cols = grid.shape
    max_len = 0
    start_row = -1
    col_index = -1

    for j in range(cols):
        current_len = 0
        current_start_row = -1
        for i in range(rows):
            if grid[i, j] == value:
                if current_len == 0:
                    current_start_row = i
                current_len += 1
            else:
                if current_len > max_len:
                    max_len = current_len
                    start_row = current_start_row
                    col_index = j
                current_len = 0
                current_start_row = -1
        # Check for line at the end of the column
        if current_len > max_len:
            max_len = current_len
            start_row = current_start_row
            col_index = j

    return start_row, col_index, max_len

def check_adjacent_whites(grid, start_row, col_index, length):
    """Checks for white pixels to the left or right of the entire blue line."""
    for i in range(length):
        row = start_row + i
        if (col_index > 0 and grid[row, col_index - 1] == 0) or \
           (col_index < grid.shape[1] - 1 and grid[row, col_index + 1] == 0):
            return True
    return False

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # 1. Find the longest blue line
    start_row, col_index, length = find_vertical_line(input_grid, 1)

    # 2. Check for adjacent whites
    has_adjacent_whites = check_adjacent_whites(input_grid, start_row, col_index, length)

    # 3. Determine output dimensions
    output_height = length
    output_width = 3 if has_adjacent_whites else 1

    # 4. Create output grid
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # 5. Populate with Azure
    center_col = 1 if output_width == 3 else 0
    for i in range(length):
        output_grid[i, center_col] = 8  # Center azure line

        row_in_input = start_row + i
        if output_width == 3:
            # Check left
            if col_index > 0 and input_grid[row_in_input, col_index - 1] == 0:
                output_grid[i, 0] = 8
            # Check right
            if col_index < input_grid.shape[1] - 1 and input_grid[row_in_input, col_index + 1] == 0:
                output_grid[i, 2] = 8

    # 6. Return the output grid
    return output_grid.tolist()