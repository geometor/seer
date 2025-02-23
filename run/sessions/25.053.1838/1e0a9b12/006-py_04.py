"""
1.  **Identify and Count:** Locate all non-zero pixels within the input grid and count them.
2.  **Collect**: Gather these non-zero pixels and store them, preserving their original value and their original input grid coordinates.
3.  **Sort**: Sort the collected pixels based first on the original input column and then the original input row, in ascending order for both.
4. **Place**: Starting at the bottom left most cell, place the sorted pixels into the last row of the output grid by iterating through all columns on that last row.
5.  **Fill**: Fill all the other cells in the output grid with the value 0.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # 1. Identify, Count and Collect non-zero pixels with their coordinates
    non_zero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_pixels.append(((r, c), input_grid[r, c]))

    # 2. Sort non-zero pixels by column, then by row
    non_zero_pixels.sort(key=lambda x: (x[0][1], x[0][0]))

    # 3. Place sorted pixels in the last row of the output grid, handling potential overflow
    last_row_index = 0
    for _, value in non_zero_pixels:
        if last_row_index < cols:  # Check if we are within the bounds of the output grid
            output_grid[rows - 1, last_row_index] = value
            last_row_index += 1
        # else: implicit else:  if we run out of space on bottom row, ignore
        # this addresses potential errors
    #4. no need to fill - since grid was initialized with zeros

    return output_grid