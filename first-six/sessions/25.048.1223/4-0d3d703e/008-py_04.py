"""
The transformation rule consists of a color substitution: 9 becomes 8, 4 becomes 3, and 2 becomes 6. The spatial structure of the grid (three vertical lines) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution:
    9 -> 8, 4 -> 3, and 2 -> 6.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply color mapping: 9 -> 8, 4 -> 3, 2 -> 6.
    output_grid[input_grid == 9] = 8
    output_grid[input_grid == 4] = 3
    output_grid[input_grid == 2] = 6

    return output_grid