"""
The transformation identifies the positions of green (3) cells in the input grid that are one cell in from the input boundary.
These positions are remapped to a 3x5 output matrix.
The output grid is filled with green color at the mapped positions, as well as filling with green positions (0,1), (0,2), (1,1) and (1,2).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on the positions of the green cells.
    """
    # Initialize an output grid
    output_grid = np.zeros((3, 5), dtype=int)

    # Find green object in the input grid.
    rows, cols = np.where(input_grid == 3)
    green_positions = list(zip(rows, cols))

    # Extract corners relative to grid boundaries.
    corners = []
    if green_positions:
      min_row = min(rows)
      max_row = max(rows)
      min_col = min(cols)
      max_col = max(cols)
      corners = [(min_row, min_col), (min_row, max_col), (max_row, min_col), (max_row, max_col)]


    # Map corner positions to output grid, and paint them green
    for r, c in corners:
       out_r = 0 if r==min_row else 2
       out_c = 0 if c==min_col else 4
       output_grid[out_r,out_c] = 3
    
    # paint green additional coordinates.
    output_grid[0,1] = 3
    output_grid[0,2] = 3
    output_grid[1,1] = 3
    output_grid[1,2] = 3

    return output_grid