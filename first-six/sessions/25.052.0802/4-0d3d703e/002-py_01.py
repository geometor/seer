"""
The transformation rule is a simple color substitution: each color in the input grid is mapped to a new color in the output grid according to the following rule:
- Green (3) -> Yellow (4)
- Blue (1) -> Gray (5)
- Red (2) -> Magenta (6)
Essentially, we add 1 to input_color to get output color.
The structure of the grid remains identical.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid into the output grid by applying a color substitution.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell in the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Get the color of the current cell.
            input_color = input_grid[i, j]

            # Apply the color substitution:  output_color = input_color + 1
            output_color = input_color + 1

            # Place the new color in the corresponding cell of the output grid.
            output_grid[i, j] = output_color

    return output_grid