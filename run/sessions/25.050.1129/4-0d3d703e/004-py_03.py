"""
The transformation rule is a color mapping where each color in the input grid is replaced by a new color in the output grid. The new color is determined by adding 4 to the original color value and taking the modulo 10 of the result. This ensures that the new color value remains within the range 0-9.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping based on adding 4 and taking modulo 10.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply the color mapping rule: new_color = (old_color + 4) % 10
            output_grid[i, j] = (input_grid[i, j] + 4) % 10

    return output_grid