"""
Counts the number of cells with value 1 (blue) in the input grid and returns the count.
"""

import numpy as np

def transform(input_grid):
    """
    Counts the number of cells with value 1 (blue) in the input grid.

    Args:
        input_grid (list of lists): A 2D array representing the input grid.

    Returns:
        int: The count of cells with value 1.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Count the number of cells with value 1.
    count = np.sum(input_array == 1)
    
    output_grid = [[count]]

    return output_grid