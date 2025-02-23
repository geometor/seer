"""
Replace all values in the input grid with the value 3.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing all its elements with the value 3.

    Args:
        input_grid (list of lists): A 2D array representing the input grid.

    Returns:
        list of lists: A 2D array representing the transformed grid, with all elements set to 3.
    """
    # initialize output_grid as a copy with the same dimensions
    output_grid = np.full_like(input_grid, 3)

    # no need to iterate - numpy can do the substitution of entire array

    return output_grid.tolist()