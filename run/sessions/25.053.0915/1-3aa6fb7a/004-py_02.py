"""
1.  **Identify Azure Lines:** Find all horizontal, contiguous lines of azure (8) pixels. A line can be of length 1 or more.
2.  **Check Right Edge:** For each azure line, check if it extends to the right edge of the grid.
    *   If the line *does not* extend to the right edge, place a single blue (1) pixel immediately to the right of the last azure pixel in that line.
3. **Check Left Edge:** For each azure line, check it extends to the left edge of the grid.
    * If the line *does not* extend to the left edge, place a single blue (1) pixel immediately to the left of the first azure pixel in that line.
4. **All other pixels:** should be 0 (white).
5.  **Output Grid:** Create a new grid with the original azure lines and the newly placed blue pixels.
"""

import numpy as np

def find_azure_lines(grid):
    azure_lines = []
    for row_index, row in enumerate(grid):
        start = -1
        for col_index, pixel in enumerate(row):
            if pixel == 8:
                if start == -1:
                    start = col_index
            elif start != -1:
                azure_lines.append((row_index, start, col_index - 1))
                start = -1
        if start != -1:  # Check for line at the end of the row
            azure_lines.append((row_index, start, len(row) - 1))
    return azure_lines

def transform(input_grid):
    # initialize output_grid as a copy of input
    output_grid = input_grid.copy()
    
    # set all non azure to zero
    output_grid[output_grid != 8] = 0

    # Find all horizontal azure lines
    azure_lines = find_azure_lines(input_grid)
    
    # Iterate through the lines and place blue pixels
    for row, start_col, end_col in azure_lines:
        # Check right edge
        if end_col + 1 < input_grid.shape[1]:
            output_grid[row, end_col + 1] = 1
        # Check left edge
        if start_col - 1 >= 0:
            output_grid[row, start_col - 1] = 1

    return output_grid