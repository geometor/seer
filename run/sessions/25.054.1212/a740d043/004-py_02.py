"""
1.  **Locate Start:** Find the top-left most non-blue pixel in the input grid. This is the starting point (row, col) for the output.
2.  **Determine output dimensions:**
    *    Start from the first non-blue pixel.
    *    Expand down, including rows, until a row of all blue is encountered.
    *   Expand right, including columns, until a column of all blue is encountered.
3.  **Extract Sub-grid:** Create an output grid using the dimensions determined. Copy the corresponding non-blue pixels from the input grid to the output grid, starting from the identified top-left non-blue pixel. Stop adding from a row or column if blue (1) pixels encountered.
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

def determine_output_dimensions(input_grid, start_row, start_col):
    """
    Determines the dimensions of the output grid based on the extent of
    non-blue pixels, stopping at blue pixels (1).
    """
    max_rows, max_cols = np.shape(input_grid)
    out_rows = 0
    out_cols = 0

    # Determine output rows
    for r in range(start_row, max_rows):
        if all(input_grid[r, start_col:] == 1):
            break
        out_rows += 1
    
    # Determine output cols
    for c in range(start_col, max_cols):
       if all(input_grid[start_row:, c] == 1):
            break
       out_cols+=1

    return out_rows, out_cols

def transform(input_grid):
    """
    Transforms the input grid by extracting a contiguous region of non-blue
    pixels, using blue pixels as boundaries.
    """
    # Find the starting point (top-left non-blue pixel)
    start_coords = get_top_left_non_blue_pixel(input_grid)
    if start_coords is None:
        return np.array([])  # Return an empty array if no non-blue pixels

    start_row, start_col = start_coords

    # Determine output dimensions
    out_rows, out_cols = determine_output_dimensions(input_grid, start_row, start_col)
   

    # Create the output grid
    output_grid = np.zeros((out_rows, out_cols), dtype=int)

    # Copy the relevant pixels
    for r in range(out_rows):
        for c in range(out_cols):
            output_grid[r, c] = input_grid[start_row + r, start_col + c]

    return output_grid