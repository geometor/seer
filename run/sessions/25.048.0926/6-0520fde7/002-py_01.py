"""
The transformation extracts the central pixel of the original shape to create a new 3x3 grid. 
It changes this extracted pixel color to red and fills the other pixels of the output grid with color white. 
It replaces the central red pixel with the number of blue objects in the second row.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid as per the described rule.
    """
    # Create an output grid with size 3x3 filled with white pixels (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Count the number of blue objects in the second row.
    blue_count = np.count_nonzero(input_grid[1, :] == 1)

    # Place blue_count in center of output grid.
    output_grid[1, 1] = blue_count
    if blue_count == 0:
        output_grid[1,1] = 0
    else:
      output_grid[1,1] = 2


    return output_grid