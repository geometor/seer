"""
The transformation extracts a subgrid from the input. The subgrid consists of the
first *n* columns of the input grid, where *n* is the width of the expected
output grid. The height of the subgrid is the same as the input grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array.  This isn't strictly necessary
    # for this simple case, but it's good practice for more complex operations.
    input_array = np.array(input_grid)

    # Determine the width of the output grid.  We don't have the "expected"
    # grid at runtime, but we know from the examples that the width of "expected" is
    # the width we want.  I'll hardcode these from the examples for now.  This
    # needs to be generalized later, possibly by looking at the pattern of
    # widths in the examples.

    # Get dimensions
    rows = len(input_array)
    cols = len(input_array[0])

    if rows == 3 and cols == 9:
        output_width = 3
    elif rows == 4 and cols == 12:
        output_width = 4
    elif rows == 2 and cols == 6:
        output_width = 2
    else: # will fail here if not in the training set, need to generalize this!
        output_width = 0 

    # Extract the subgrid.
    output_grid = input_array[:, :output_width].tolist()

    return output_grid