"""
The output is a direct copy of the upper-left 3x3 portion (the top three rows) of the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the top 3x3 subgrid from the input grid.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Extract the top 3x3 subgrid.
    output_array = input_array[:3, :3]

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid