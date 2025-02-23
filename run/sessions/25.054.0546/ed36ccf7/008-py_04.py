"""
The transformation rule is a 90-degree counter-clockwise rotation of the input grid.
"""

import numpy as np

def rotate_grid_ccw(grid):
    """Rotates a 2D grid 90 degrees counter-clockwise."""
    return np.rot90(grid)

def transform(input_grid):
    """
    Transforms the input grid by rotating it 90 degrees counter-clockwise.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Rotate the array counter-clockwise.
    output_array = rotate_grid_ccw(input_array)

    # Convert the NumPy array back to a list.
    output_grid = output_array.tolist()

    return output_grid