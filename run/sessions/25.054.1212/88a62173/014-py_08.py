"""
The transformation extracts a 2x2 representation of the larger, somewhat checkerboard-like input grid by taking top-left corner and using it's simplified 2x2 pattern.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as 2x2 numpy array with zeros
    output_grid = np.zeros((2, 2), dtype=int)

    # Extract the top-left 2x2 subgrid from the input
    subgrid = input_grid[:2, :2]

    # check if top left 2 x 2 has alternating pattern, if yes, use it, if no, use general rule
    if (subgrid[0,0] != subgrid[0,1]) and (subgrid[0,0] != subgrid[1,0]) and (subgrid[1,1] != subgrid[1,0]) and (subgrid[1,1] != subgrid[0,1]):
      output_grid = subgrid
    else:
        # Apply the alternating pattern to the output
        output_grid[0, 0] = input_grid[0, 0]
        output_grid[0, 1] = input_grid[0, -1]
        output_grid[1, 0] = input_grid[-1, 0]
        output_grid[1, 1] = input_grid[-1, -1]

    return output_grid