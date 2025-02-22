"""
The transformation rule is a color substitution with a specific rule for the color 9:
- If the input color is less than 9, increment it by 1.
- If the input color is 9, change it to 8.
The grid structure remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid into the output grid by applying a color substitution with a special rule for 9.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell in the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Get the color of the current cell.
            input_color = output_grid[i, j]

            # Apply the color substitution:
            # If the color is 9, set it to 8.
            # Otherwise, increment it by 1.
            if input_color == 9:
                output_color = 8
            else:
                output_color = input_color + 1

            # Place the new color in the corresponding cell of the output grid.
            output_grid[i, j] = output_color

    return output_grid