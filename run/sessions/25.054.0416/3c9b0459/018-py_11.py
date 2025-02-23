"""
The transformation rule is a cyclic upward shift of the rows of the input grid. The first row becomes the last row, the second row becomes the first row, and so on. In general terms, for an input grid of *n* rows, the row at index *i* in the output grid is the row at index *(i+1) mod n* in the input grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)

    # shift rows up cyclically
    output_np = np.roll(input_np, shift=-1, axis=0)

    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()
    return output_grid