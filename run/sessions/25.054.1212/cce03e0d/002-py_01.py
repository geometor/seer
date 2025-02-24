"""
The transformation rule is to expand the input grid into a 9x9 grid. The original input grid's content is placed in the top-left corner of the output grid, and the rest of the output grid is filled with zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Expands the input grid to a 9x9 grid, placing the input in the top-left corner.
    
    Parameters:
    input_grid (numpy.ndarray): A 2D numpy array representing the input grid.
    
    Returns:
    numpy.ndarray: The expanded 9x9 output grid.
    """
    # initialize output_grid as a 9x9 array filled with 0s
    output_grid = np.zeros((9, 9), dtype=int)

    # get dimensions of input grid
    rows, cols = input_grid.shape

    # copy the input grid to the top-left corner of output grid
    output_grid[:rows, :cols] = input_grid

    return output_grid