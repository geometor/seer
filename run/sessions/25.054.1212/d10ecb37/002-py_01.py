"""
Extracts the 2x2 subgrid from the top-left corner of the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the 2x2 subgrid from the top-left corner of the input.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The 2x2 subgrid extracted from the input.
    """
    # Convert the input list of lists to a NumPy array for easier slicing.
    input_array = np.array(input_grid)

    # Extract the 2x2 subgrid from the top-left corner.
    output_array = input_array[0:2, 0:2]

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid