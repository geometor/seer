"""
Extract the top-left 2x2 subgrid from the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the 2x2 subgrid at the top-left corner of the input grid.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid[0:2, 0:2]  # Slice the top-left 2x2 region
    return output_grid.tolist()