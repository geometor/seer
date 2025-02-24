"""
1.  **Locate Starting Point:** Find the top-left most non-blue pixel in the input grid. This is the initial starting point (row, col).

2.  **Determine Bounding Box:**
    *   From the starting point, expand downwards until you encounter a fully blue row. The row *before* the fully blue row is the bottom boundary.
    *   From the starting point, expand to the right until you encounter a fully blue column. The column *before* the fully blue column is the right boundary.
    *   The top boundary is the row of the starting point.
    *  The left boundary is the column of the starting point.

3.  **Extract Sub-grid:** Create an output grid with the dimensions defined by the bounding box.

4. **Fill Output:**
    *  Iterate through the bounding box area in the original grid.
    *  If a cell is not blue, replace it with a zero.
    *  Copy the cells of the original grid into the output.
"""

import numpy as np

def get_top_left_non_blue_pixel(grid):
    """
    Returns the (row, col) tuple of the top-left most non-blue pixel.
    Returns None if no non-blue pixels are found.
    """
    rows, cols = np.shape(grid)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                return (r, c)
    return None

def determine_bounding_box(input_grid, start_row, start_col):
    """
    Determines the bounding box of the region of interest.
    """
    max_rows, max_cols = np.shape(input_grid)
    bottom_row = start_row
    right_col = start_col

    # Expand downwards
    for r in range(start_row + 1, max_rows):
        if all(input_grid[r, :] == 1):
            break
        bottom_row = r

    # Expand to the right
    for c in range(start_col + 1, max_cols):
        if all(input_grid[:, c] == 1):
            break
        right_col = c

    return start_row, start_col, bottom_row, right_col

def transform(input_grid):
    """
    Transforms the input grid by extracting a contiguous region of non-blue
    pixels, using solid blue rows/columns as boundaries, and sets to zero
    pixels in the output grid if they are not blue.
    """
    # Find the starting point (top-left non-blue pixel)
    start_coords = get_top_left_non_blue_pixel(input_grid)
    if start_coords is None:
        return np.array([])  # Return an empty array if no non-blue

    start_row, start_col = start_coords

    # Determine the bounding box
    top_row, left_col, bottom_row, right_col = determine_bounding_box(input_grid, start_row, start_col)

    # Create the output grid
    out_rows = bottom_row - top_row + 1
    out_cols = right_col - left_col + 1
    output_grid = np.zeros((out_rows, out_cols), dtype=int)

    # Copy and modify pixels within the bounding box
    for r in range(out_rows):
        for c in range(out_cols):
            original_value = input_grid[top_row + r, left_col + c]
            output_grid[r,c] = original_value

    return output_grid