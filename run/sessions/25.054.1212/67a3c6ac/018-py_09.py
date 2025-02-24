"""
The transformation rule involves reversing the order of rows and then reversing the order of columns within each row.
It's equivalent to performing a 180-degree rotation, but described here as independent row and column reversals.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by reversing rows and then reversing columns.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the grid.
    rows, cols = input_grid.shape
    
    # Reverse the order of the rows.
    output_grid = output_grid[::-1, :]
    
    # Reverse the order of the columns within each row.
    output_grid = output_grid[:, ::-1]

    return output_grid