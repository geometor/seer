"""
Invert the color of all pixels in the input grid to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by inverting the color of all pixels.
    
    Args:
        input_grid (numpy.ndarray): A 2D numpy array representing the input grid.
        
    Returns:
        numpy.ndarray: A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = input_grid.copy()
    
    # Get the dimensions of the grid.
    rows, cols = output_grid.shape
    
    # Iterate through each pixel in the grid.
    for i in range(rows):
        for j in range(cols):
            # Invert the pixel value.  If 0, change to 1. If 1, change to 0.
            if output_grid[i, j] == 0:
                output_grid[i, j] = 1
            else:
                output_grid[i, j] = 0
                
    return output_grid