"""
1.  **Identify**: Locate all non-zero pixels within the input grid.
2.  **Collect**: Gather these non-zero pixels, preserving their original values.
3.  **Sort**: Sort the collected pixels based on original column, then original row, in ascending order.
4.  **Place**: Position the sorted pixels along the bottom row of the output grid, filling cells from left to right.
5.  **Fill**: All other cells in output grid default to value of 0.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by moving all non-zero elements to the bottom row,
    preserving their order from left to right and top to bottom.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # 1. Identify and Collect non-zero pixels with their coordinates
    non_zero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_pixels.append(((r, c), input_grid[r, c]))

    # 2. Sort non-zero pixels by column, then by row
    non_zero_pixels.sort(key=lambda x: (x[0][1], x[0][0]))

    # 3. Place sorted pixels in the last row of the output grid
    last_row_index = 0
    for _, value in non_zero_pixels:
        output_grid[rows - 1, last_row_index] = value
        last_row_index += 1

    return output_grid