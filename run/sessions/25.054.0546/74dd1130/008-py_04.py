"""
The transformation is a swap between the pixel located at (1,2) and (2,0). The rest of the pixels keep their position.
"""

import numpy as np

def transform(input_grid):
    """
    Swaps the values at (1,2) and (2,0) in a 3x3 grid.
    
    Args:
      input_grid: A 3x3 numpy array representing the input grid.
      
    Returns:
      A 3x3 numpy array with the specified swap.
    """
    output_grid = input_grid.copy()

    # Swap elements at (1,2) and (2,0)
    temp = output_grid[1, 2]
    output_grid[1, 2] = output_grid[2, 0]
    output_grid[2, 0] = temp

    return output_grid