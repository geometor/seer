"""
Isolates a pre-existing vertical azure (8) column within the input grid, 
setting all other pixels to grey (0).
"""

import numpy as np

def find_vertical_column(grid, color):
    """
    Finds the x-coordinate of a vertical column of the specified color.
    Returns -1 if no such column is found.
    """
    height, width = grid.shape
    for x in range(width):
        is_column = True
        for y in range(height):
            if grid[y, x] != color:
                is_column = False
                break
        if is_column:
            return x
    return -1

def transform(input_grid):
    """
    Transforms the input grid by isolating the azure column and setting
    all other pixels to grey.
    """
    # Initialize the output grid with all grey pixels.
    output_grid = np.zeros_like(input_grid)

    # Find the x-coordinate of the azure (8) column.
    azure_column_x = find_vertical_column(input_grid, 8)

    # If an azure column is found, copy it to the output grid.
    if azure_column_x != -1:
        height = input_grid.shape[0]
        for y in range(height):
            output_grid[y, azure_column_x] = 8

    return output_grid