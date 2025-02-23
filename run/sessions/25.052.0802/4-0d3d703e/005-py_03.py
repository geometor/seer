"""
The transformation rule is a color substitution: each color in the input grid is mapped to a new color in the output grid according to the following rule:
- Red (2) -> Magenta (6)
- Green (3) -> Yellow (4)
- Azure (8) -> Maroon (9)
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

            # Apply the color substitution.
            if input_color == 2:
                output_color = 6
            elif input_color == 3:
                output_color = 4
            elif input_color == 8:
                output_color = 9
            else:
                output_color = input_color # added to ensure the function completes for any color

            # Place the new color in the corresponding cell of the output grid.
            output_grid[i, j] = output_color

    return output_grid