"""
The transformation rule is to perform a complete color swap of magenta (6) and green (3).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping all instances of magenta (6) with green (3) and vice versa.

    Args:
        input_grid (numpy.ndarray): The input grid as a 2D numpy array.

    Returns:
        numpy.ndarray: The transformed grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Swap magenta (6) with green (3).
    output_grid[input_grid == 6] = 3
    output_grid[input_grid == 3] = 6
    #note: need a temp variable to swap in place correctly

    return output_grid