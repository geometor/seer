"""
The transformation rule consists of a color substitution: 2 becomes 6, 3 becomes 4, and 8 becomes 9. The spatial structure of the grid (three vertical lines) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution:
    2 -> 6, 3 -> 4, and 8 -> 9.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply color mapping: 2 -> 6, 3 -> 4, 8 -> 9.
    output_grid[input_grid == 2] = 6
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 8] = 9

    return output_grid