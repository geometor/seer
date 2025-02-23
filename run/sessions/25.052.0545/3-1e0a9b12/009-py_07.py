"""
Moves objects to the bottom of the grid, preserving vertical stacks and column order, then filling the rest with white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving objects to the bottom, maintaining vertical stacks and column order.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    for col in range(cols):
        # Extract non-zero elements and their vertical connections
        column_elements = []
        i = 0
        while i < rows:
            if input_grid[i, col] != 0:
                start_row = i
                end_row = i
                while end_row + 1 < rows and input_grid[end_row + 1, col] == input_grid[start_row, col]:
                    end_row += 1
                column_elements.append((input_grid[start_row, col], end_row - start_row + 1))
                i = end_row + 1
            else:
                i += 1

        # Place elements at the bottom of the output column
        current_row = rows - 1
        for value, height in reversed(column_elements):
            output_grid[current_row - height + 1:current_row + 1, col] = value
            current_row -= height

    return output_grid