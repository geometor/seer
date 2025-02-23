"""
The transformation rule consists of a color substitution: 5 becomes 1, 8 becomes 9, and 6 becomes 2. The spatial structure of the grid (three vertical lines) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution:
    5 -> 1, 8 -> 9, and 6 -> 2.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply color mapping: 5 -> 1, 8 -> 9, 6 -> 2.
    output_grid[input_grid == 5] = 1
    output_grid[input_grid == 8] = 9
    output_grid[input_grid == 6] = 2

    return output_grid