"""
1.  **Find Blue Pixel:** Locate the single blue pixel (value 1) in the input grid and record its row and column indices.
2.  **Initialize Output:** Create an output grid of the same dimensions as the input grid, initially filled with white pixels (value 0).
3.  **Transform Row and Column:**
    *   Iterate through each cell index, i, in the row.
    *   If the cell index, i, has the same value (mod 2) of the blue pixel's column index, replace the value of the cell with blue(1).
    *    Iterate through each cell index, j, in the column.
    *   If the cell index, j, has the same value (mod 2) of the blue pixel's row index, replace the value of the cell with blue(1).
4.  **Skip Center:** The original blue pixel's location in the output grid remains unchanged(from the init to all 0s) .
5. **Return Output:** Return the modified output grid.
"""

import numpy as np

def find_blue_pixel(grid):
    # Find the coordinates of the blue pixel (value 1).
    for r_idx, row in enumerate(grid):
        for c_idx, pixel in enumerate(row):
            if pixel == 1:
                return r_idx, c_idx
    return None

def transform(input_grid):
    # Initialize output_grid as all white.
    output_grid = np.zeros_like(input_grid)

    # Find the blue pixel's location.
    blue_pixel_location = find_blue_pixel(input_grid)

    if blue_pixel_location:
        center_row, center_col = blue_pixel_location

        # Transform the row.
        for c_idx in range(output_grid.shape[1]):
            if c_idx % 2 == center_col % 2:
                output_grid[center_row, c_idx] = 1

        # Transform the column.
        for r_idx in range(output_grid.shape[0]):
            if r_idx % 2 == center_row % 2:
                output_grid[r_idx, center_col] = 1

    return output_grid