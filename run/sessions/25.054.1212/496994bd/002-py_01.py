"""
The transformation takes the top three rows of the input and mirrors/inverts it, placing the added section it to the bottom of the grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by inverting and appending a copy of the top three rows to the bottom.
    """
    # Convert input_grid to a NumPy array for easier manipulation
    input_grid = np.array(input_grid)

    # Get the dimensions of the input grid
    rows, cols = input_grid.shape

    # Initialize the output grid as a copy of the input grid
    output_grid = input_grid.copy()
    
    # Extract the top three rows
    top_rows = input_grid[0:3, :]
    
    #Invert the top section
    inverted_rows = np.flipud(top_rows)

    # Append the inverted section to the bottom of the output grid
    output_grid = np.concatenate((output_grid, inverted_rows), axis=0)

    return output_grid.tolist()