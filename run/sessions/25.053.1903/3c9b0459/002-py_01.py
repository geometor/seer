"""
The transformation is a 180-degree rotation of the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid by 180 degrees.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The rotated grid.
    """
    # Convert the input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Rotate the array by 180 degrees (two 90-degree rotations)
    rotated_array = np.rot90(input_array, 2)

    # Convert the rotated array back to a list of lists
    output_grid = rotated_array.tolist()

    return output_grid