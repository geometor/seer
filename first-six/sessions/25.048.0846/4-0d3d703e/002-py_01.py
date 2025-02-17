"""
The transformation rule is a color substitution where each cell's color value in the input grid is incremented by 1 (modulo 10) to produce the corresponding cell's color in the output grid. The structure and position of the colored regions remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by incrementing each cell's color value by 1 (modulo 10).

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The transformed output grid.
    """
    # Convert the input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Initialize the output grid as a copy of the input grid
    output_array = np.copy(input_array)

    # Apply the color transformation: increment each color value by 1 (modulo 10)
    output_array = (output_array + 1) % 10

    # Convert the NumPy array back to a list of lists
    output_grid = output_array.tolist()

    return output_grid