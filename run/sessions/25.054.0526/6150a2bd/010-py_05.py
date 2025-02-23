"""
The transformation rule involves reflecting the input grid horizontally across its vertical axis. For a 3x3 grid, this means that the first column swaps with the third column, while the middle column remains in place. The color of each pixel is preserved during this reflection. Specifically, the pixel at `input[row][col]` moves to `output[row][2 - col]`.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a 3x3 input grid into a 3x3 output grid by reflecting it horizontally.

    Args:
        input_grid (list of lists): A 3x3 grid represented as a list of lists.

    Returns:
        list of lists: The transformed 3x3 grid.
    """
    # Initialize the output grid as a 3x3 matrix filled with zeros
    output_grid = [[0, 0, 0] for _ in range(3)]
    n = len(input_grid)

    # Iterate through each cell of the input grid
    for i in range(n):
        for j in range(n):
            # Calculate the new column index for horizontal reflection
            new_j = n - 1 - j

            # Assign colors of input pixels to the reflected output pixels
            output_grid[i][new_j] = input_grid[i][j]

    return output_grid