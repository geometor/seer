"""
The output grid is created by taking the leftmost one-third of the input grid's columns.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a numpy array
    output_grid = np.array(input_grid)

    # calculate the output width: input width / 3
    input_width = output_grid.shape[1]
    output_width = int(input_width / 3) # round to remove decimal

    # crop the grid by taking all rows and the first output_width columns
    output_grid = output_grid[:, :output_width]
    
    return output_grid.tolist() # return as a list