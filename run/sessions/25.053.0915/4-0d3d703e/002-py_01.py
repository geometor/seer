"""
The input is a 3x3 grid. Each value in the input grid is replaced by its corresponding mapped value: 1 (blue) becomes 4 (yellow), 2 (red) becomes 5 (gray), and 3 (green) becomes 6 (magenta). The output is the same size grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by applying a value substitution based on a predefined mapping.
    """
    # Initialize the output grid as a copy of the input grid to preserve dimensions.
    output_grid = np.copy(input_grid)

    # Define the mapping dictionary.
    mapping = {
        1: 4,  # blue -> yellow
        2: 5,  # red -> gray
        3: 6   # green -> magenta
    }

    # Iterate through the input grid and apply the mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            output_grid[i, j] = mapping.get(output_grid[i, j], output_grid[i,j]) #use .get() and self for the default

    return output_grid