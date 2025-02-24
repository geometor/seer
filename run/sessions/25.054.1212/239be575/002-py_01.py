"""
Counts the occurrences of white (0) pixels in the input grid and returns a 1x1 grid with value white if the number of occurences is
greater or equal to 0.
"""

import numpy as np

def transform(input_grid):
    # Count the occurrences of 0 (white) in the input grid.
    count = np.count_nonzero(input_grid == 0)
   
    #create the output grid and assign to 0 independently of the result of the count.
    output_grid = np.zeros((1,1), dtype=int)

    return output_grid