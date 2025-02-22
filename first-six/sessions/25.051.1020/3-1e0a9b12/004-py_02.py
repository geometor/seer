"""
1. Identify Objects: Consider all colored cells (non-zero values) as individual objects.

2. Gravity within Columns: For each column, independently:
    *   Treat the bottom row as the "ground."
    *   Any object above the "ground" will fall (move down) to the lowest unoccupied cell within its current column.
    *   Objects maintain their original vertical order within each column; that is, if object A is above object B in the input, and both must fall, A will still be above B in the output.

3. Preservation: If the lowest cell is already occupied in a column, do not overide it, stack on top of it.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each column
    for col in range(cols):
        # Get the non-zero elements in the current column, preserving order
        column_objects = [(row, input_grid[row, col]) for row in range(rows) if input_grid[row, col] != 0]

        # Simulate gravity: place objects at the bottom of the column
        output_row = rows - 1
        for row, color in reversed(column_objects):  # Reverse to maintain order
            output_grid[output_row, col] = color
            output_row -= 1 # decrement to implement stacking

    return output_grid