"""
The transformation involves two primary actions. Firstly, The cells with color code 2 (red) is replaced with the color 7 (orange) object, causing it to merge/expand with the original orange object.. Secondly, the entire background, originally white (color 0), is changed to green (color 3), while the combined orange object remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)

    # Replace all instances of color 2 with color 7.
    output_grid[output_grid == 2] = 7

    # Create a new grid filled with color 3 (green).
    new_output_grid = np.full(input_grid.shape, 3)

    # Copy the orange (color 7) object from output_grid to new_output_grid.
    new_output_grid[output_grid == 7] = 7

    return new_output_grid