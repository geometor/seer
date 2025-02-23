"""
The output grid is created by taking the leftmost portion of the input grid. Specifically, take the first four columns of the input grid to form the output grid. This is a simple horizontal cropping operation.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a numpy array
    output_grid = np.array(input_grid)

    # crop the grid by taking all rows and the first four columns
    output_grid = output_grid[:, :4]
    
    return output_grid.tolist() # return as a list