"""
The output grid is a 10x10 section extracted from the bottom-left corner of the 21x21 input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 10x10 subgrid from the bottom-left corner of the input grid.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Determine the dimensions of the input grid.
    rows, cols = input_array.shape

    # Define the size of the output grid.
    output_size = 10

    # Extract the 10x10 subgrid from the bottom-left.
    output_grid = input_array[rows-output_size:, :output_size]
    
    return output_grid.tolist()