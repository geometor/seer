"""
Removes all pixels with a value of 0 (white) from the input grid, effectively
shrinking the grid where white pixels existed.
"""

import numpy as np

def transform(input_grid):
    """
    Removes all white (0) pixels from the input grid, altering grid dimensions.
    """
    # Convert the input grid to a list of lists for easier manipulation.
    input_list = input_grid.tolist()
    output_list = []

    # Iterate through rows
    for row in input_list:
      # filters through a list comprehension
      new_row = [pixel for pixel in row if pixel != 0]
      output_list.append(new_row)

    # Convert the result back to a NumPy array.  Handle cases where rows
    # might have different lengths after removing 0s.  If rows are of
    # unequal length, NumPy will create an array of `object` dtype, which
    # isn't what we intend. So, we convert each sublist back to its own array.
    output_grid = np.array([np.array(row) for row in output_list], dtype=object)
    return output_grid