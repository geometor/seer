"""
1.  **Copy Top Rows:** Copy the first three rows (rows 0, 1, and 2) of the input grid to the output grid without modification.
2.  **Find Horizontal Line:** Starting from row 3, search for the first horizontal line. A horizontal line is defined as a row where all pixels have the same non-zero color.
3.  **Preserve Horizontal Line (if found):** If a horizontal line is found, copy that entire row from the input grid to the corresponding row in the output grid.
4.  **Blank Subsequent Rows:**  All rows *below* the first three rows, are set to 0 (white).
5. **Blank Rows After Horizontal Line (if present)**: All rows below the copied horizontal line are set to all 0 (white).
"""

import numpy as np

def is_horizontal_line(grid, row):
    """Checks if a given row in the grid forms a horizontal line (all pixels have the same non-zero color)."""
    if row < 0 or row >= grid.shape[0]:
        return False
    first_color = grid[row, 0]
    if first_color == 0:  # Consider 0 as background, not a line
       return False
    for col in range(1, grid.shape[1]):
        if grid[row, col] != first_color:
            return False
    return True

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.zeros_like(input_grid)

    # 1. Preserve Top Rows
    for row in range(min(3, input_grid.shape[0])):
        output_grid[row, :] = input_grid[row, :]

    # 2 & 3. Find and Preserve Horizontal Line
    found_horizontal_line = False
    horizontal_line_row = -1
    for row in range(3, input_grid.shape[0]):
        if not found_horizontal_line and is_horizontal_line(input_grid, row):
            output_grid[row, :] = input_grid[row, :]
            found_horizontal_line = True
            horizontal_line_row = row

    # 4 & 5. Blanking rows after horizontal line or after the first three rows
    for row in range(3, input_grid.shape[0]):
        if found_horizontal_line:
            if row > horizontal_line_row:
               output_grid[row,:] = 0 #blank
        else: #no horizontal line found, so blank after top 3
            output_grid[row,:] = 0

    return output_grid