"""
Extract a 5x5 sub-grid from the top-left corner of the input grid, and keeps pixels of color white and green, which becomes the output.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 5x5 sub-grid from the top-left corner of the input grid.
    Keeps only white (0) and green (3) pixels.
    """
    # Initialize the output grid (not strictly necessary here, but good practice)
    # output_grid = np.zeros((5, 5), dtype=int)

    # Extract the 5x5 sub-grid.  Direct slicing is the most efficient way.
    output_grid = input_grid[0:5, 0:5]
    
    #Create mask
    mask = np.logical_or(output_grid == 0, output_grid == 3)

    # Apply the mask to keep only 0s and 3s
    output_grid = np.where(mask, output_grid, 0)  #Could be any value outside the mask
   

    return output_grid