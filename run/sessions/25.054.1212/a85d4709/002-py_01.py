"""
Replaces values in the input grid according to the following rules:
- 0 is replaced with 3.
- 5 is replaced with 2.
- Any other value is replaced with 4.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing values based on a predefined mapping.

    Args:
        input_grid (list of lists): A 3x3 grid represented as a list of lists.

    Returns:
        list of lists: The transformed 3x3 grid.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            # Apply the value replacement rules.
            if input_grid[i][j] == 0:
                output_grid[i][j] = 3
            elif input_grid[i][j] == 5:
                output_grid[i][j] = 2
            else:
                output_grid[i][j] = 4

    return output_grid