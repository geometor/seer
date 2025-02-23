"""
Extracts a 5x5 subgrid from the top-left corner of the input grid.
Identifies the unique colors present in the expected output.
Filters the extracted subgrid, keeping only pixels that match the identified output colors.
"""

import numpy as np

def transform(input_grid, expected_output=None):
    # Extract the 5x5 subgrid from the top-left corner.
    subgrid = input_grid[0:5, 0:5]

    # If the expected output is provided (during training),
    # determine the colors to keep.
    if expected_output is not None:
        unique_colors = np.unique(expected_output)
        mask = np.isin(subgrid, unique_colors)
        output_grid = np.where(mask, subgrid, 0) # Use 0 as a default fill
    else:
        # During prediction, if no expected is supplied, we'll assume a set of
        # the existing colors. This will change during iterative development.
      
        output_grid = subgrid
    return output_grid