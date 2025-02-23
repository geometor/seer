"""
Moves all non-zero pixels in the input grid to the last row of the output grid,
preserving their original column order.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid, but filled with zeros.
    output_grid = np.zeros_like(input_grid)
    
    # Get the last row index.
    last_row_index = output_grid.shape[0] - 1

    # Create a list to hold (column, value) pairs for sorting.
    non_zero_pixels = []

    # Iterate through the input grid to find non-zero pixels.
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value != 0:
                non_zero_pixels.append((col_index, value))

    # Sort the non-zero pixels by their column index.
    non_zero_pixels.sort()

    # Place the sorted non-zero pixels in the last row.
    for col_index, value in non_zero_pixels:
        output_grid[last_row_index, col_index] = value
    
    return output_grid