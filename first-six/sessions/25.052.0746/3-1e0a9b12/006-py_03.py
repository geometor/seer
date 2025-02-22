"""
The transformation involves moving all non-zero colored cells to the lowest
available row in their respective columns while maintaining their original
color and x-coordinate. Stack the objects by column, maintaining its original
order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the
    last row available, preserving their original x-coordinates and colors,
    and stacking them based on their initial order if they share a column.
    """
    # Initialize the output grid as a copy of the input grid with all zeros.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Create a dictionary to store the next available row index for each column.
    next_available_row = {col: rows - 1 for col in range(cols)}

    # Store non-zero cells with their original row index for sorting.
    cells_to_move = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                cells_to_move.append((r, c, input_grid[r, c]))

    # Sort cells by column and then by original row index (ascending).
    cells_to_move.sort(key=lambda x: (x[1], x[0]))

    # Iterate through the sorted non-zero cells and place them in the output grid.
    for r, c, color in cells_to_move:
        # Get the next available row index for the current column.
        row_index = next_available_row[c]
        # Place the cell in the output grid.
        output_grid[row_index, c] = color
        # Update the next available row index for this column.
        next_available_row[c] -= 1

    return output_grid