"""
The program filters the input grid, keeping only the azure (8) pixels and setting all other pixels to white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by keeping only pixels of color 8 and setting others to 0.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The transformed grid.
    """
    # Initialize the output grid with the same dimensions as the input grid, filled with 0s.
    output_grid = np.zeros_like(input_grid)

    # Iterate through the input grid.
    for row_index, row in enumerate(input_grid):
        for col_index, pixel_value in enumerate(row):
            # Check if the pixel's color is 8 (azure).
            if pixel_value == 8:
                # If it is, keep the pixel's value in the output grid.
                output_grid[row_index, col_index] = 8

    return output_grid