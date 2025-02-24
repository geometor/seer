"""
1.  **Identify Source Rows**: Examine the bottom three rows of the input grid.
2.  **Check for Empty Source:** If *all* pixels within the source rows are 0 (white), then the output is an empty grid.
3.  **Determine Width:** If there are any non-zero pixels within the *source rows*, calculate the width of the output grid. Find the leftmost and rightmost columns containing non-zero pixels within the source rows. The width is the difference between these column indices plus one.
4.  **Extract Pattern:** Create a new grid with a height of three and the calculated width. Copy the pixel color values from the *source rows* into the new grid, maintaining their relative horizontal positions.
5. **Double Width**: Create a new output grid with double the width from step 3.
6.  **Replicate Pattern:** Copy the extracted pattern (from step 4) to the right of the original pattern's location in the output grid.
"""

import numpy as np

def transform(input_grid):
    # Create a NumPy array from the input grid
    input_array = np.array(input_grid)

    # 1. Identify Source Rows: Focus on bottom three rows of the input
    rows, cols = input_array.shape
    start_row = max(0, rows - 3)  # Ensure start_row is not negative

    # 2. Check for Empty Source
    source_rows = input_array[start_row:rows, :]
    if np.all(source_rows == 0):
        return []

    # 3. Determine Width: Calculate width based on non-zero columns in source rows
    non_zero_cols = np.where(np.any(source_rows != 0, axis=0))[0]

    if non_zero_cols.size > 0:  # Check for non zero columns
        leftmost_col = non_zero_cols[0]
        rightmost_col = non_zero_cols[-1]
        new_width = rightmost_col - leftmost_col + 1
    else:
      return [] # should never get here because of step 2, but keeping for safety

    # 4. Extract Pattern & 5. Double Width
    output_grid = np.zeros((3, new_width * 2), dtype=int)
    output_grid[0:3, 0:new_width] = input_array[start_row:rows, leftmost_col:rightmost_col + 1]

    # 6. Replicate Pattern: Copy the extracted pattern to the right
    output_grid[0:3, new_width:new_width*2] = output_grid[0:3, 0:new_width]

    return output_grid.tolist()