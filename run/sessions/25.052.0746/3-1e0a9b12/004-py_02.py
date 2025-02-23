"""
Non-zero colored objects are moved down to the lowest available position in their respective columns, maintaining their color and x-coordinate. If there is a stack of objects of the same color they are grouped.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the
    last row available, preserving their original x-coordinates and colors.
    """
    # Initialize the output grid as a copy of the input grid with all zeros.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Create a dictionary to store the next available row index for each column.
    next_available_row = {col: rows - 1 for col in range(cols)}

    # Iterate through the input grid to find and move non-zero cells.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                # Get the color of the current cell.
                color = input_grid[r, c]
                # Get the next available row index for the current column.
                row_index = next_available_row[c]
                # Place the cell in the output grid.
                output_grid[row_index, c] = color
                # Update the next available row index for this column.
                next_available_row[c] -= 1

    return output_grid