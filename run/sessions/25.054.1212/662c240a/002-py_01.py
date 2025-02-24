"""
Extract the bottom-right 3x3 subgrid from the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the bottom-right 3x3 subgrid of the input grid.
    
    Args:
        input_grid (numpy.ndarray): The input grid.
    
    Returns:
        numpy.ndarray: The bottom-right 3x3 subgrid.
    """
    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape
    
    # Calculate the starting row and column indices for the 3x3 subgrid.
    start_row = rows - 3
    start_col = cols - 3
    
    # Extract the 3x3 subgrid.
    output_grid = input_grid[start_row:rows, start_col:cols]
    
    return output_grid