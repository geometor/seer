"""
The output is a 1x1 grid. The value of the output pixel corresponds to the
number of non-zero pixels in the input grid, incremented by one. In other
words: count the colored pixels in the input, then add 1 to get the output
value.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid into a 1x1 output grid.  The output pixel's value
    is the number of non-zero pixels in the input grid plus one.
    """
    # Convert the input to a NumPy array for easier processing
    input_grid = np.array(input_grid)

    # Count the number of non-zero pixels
    non_zero_count = np.count_nonzero(input_grid)

    # Calculate the output value (non-zero count + 1)
    output_value = non_zero_count + 1

    # Create the 1x1 output grid
    output_grid = np.array([[output_value]])

    return output_grid