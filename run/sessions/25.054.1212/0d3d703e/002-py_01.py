"""
The transformation rule is a simple mapping: 3 -> 4, 1 -> 5, 2 -> 6.
Essentially, each number in the input grid is replaced by a different, specific number in the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified mapping.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Apply the mapping to each element of the grid
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 1] = 5
    output_grid[input_grid == 2] = 6

    return output_grid