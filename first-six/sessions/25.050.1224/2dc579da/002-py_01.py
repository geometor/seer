"""
The transformation rule is: Extract the 2x2 bottom-left corner of the original grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the 2x2 subgrid from the bottom-left corner of the input grid.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Get the dimensions of the input array.
    rows, cols = input_array.shape

    # Extract the 2x2 subgrid from the bottom-left corner.
    output_grid = input_array[rows-2:rows, 0:2]
    
    return output_grid.tolist()