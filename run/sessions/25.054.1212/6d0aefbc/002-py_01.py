"""
The transformation rule duplicates each column of the input grid horizontally.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by duplicating each column horizontally.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The transformed grid with duplicated columns.
    """
    # Convert the input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Get the dimensions of the input grid
    rows, cols = input_array.shape

    # Initialize the output grid as a NumPy array with twice the width
    output_array = np.zeros((rows, cols * 2), dtype=input_array.dtype)

    # Iterate through the columns of the input grid
    for i in range(cols):
        # Duplicate each column into the output grid
        output_array[:, 2 * i] = input_array[:, i]
        output_array[:, 2 * i + 1] = input_array[:, i]

    # Convert the output NumPy array back to a list of lists
    output_grid = output_array.tolist()

    return output_grid