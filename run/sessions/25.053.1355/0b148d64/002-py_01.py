"""
The transformation extracts a rectangular region from the input grid. This region is defined by the boundaries of a contiguous red (color 2) shape located in the bottom section of the input grid. The top-left corner of the output corresponds to the top-left corner of the bounding box of this red shape.  The bottom edge of the output is the same as the bottom edge of the input. The right edge appears to be a fixed column.
"""

import numpy as np

def find_object_bounds(grid, color):
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None  # Handle cases with no object of the specified color
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier manipulation
    input_grid = np.array(input_grid)

    # Find the boundaries of the red (color 2) object
    bounds = find_object_bounds(input_grid, 2)
    if bounds is None:
        return [[]] # Return empty grid to signal that object not found
    min_row, max_row, min_col, max_col = bounds

    # Determine the output grid's dimensions and initialize it
    # The right boundary is fixed, based on observation and will be 10, counting from 1, or index 9.

    right_col = 9
    output_grid = input_grid[min_row : max_row + 1, min_col : right_col + 1].tolist()
    

    return output_grid