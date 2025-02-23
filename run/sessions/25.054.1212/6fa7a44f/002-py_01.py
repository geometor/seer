"""
The transformation rule is to repeat the input grid once vertically. The output is the input grid with itself appended below.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # change output pixels 
    output_grid = np.concatenate((output_grid, input_grid), axis=0)

    return output_grid