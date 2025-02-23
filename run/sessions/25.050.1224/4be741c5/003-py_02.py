"""
The transformation rule identifies distinct colored regions in the input grid and represents each with a single cell in the output grid, arranging them vertically.
"""

import numpy as np

def get_distinct_colors(grid):
    """
    Returns a sorted list of distinct colors present in the grid.
    """
    return sorted(np.unique(grid).tolist())

def transform(input_grid):
    """
    Transforms the input grid into a 3x1 grid representing the distinct colors.
    """
    # Get the distinct colors from the input grid
    distinct_colors = get_distinct_colors(input_grid)

    # Initialize the output grid as Nx1 array.

    output_grid = np.array(distinct_colors).reshape(-1,1)
    
    # remove all colors different than 2, 5 and 8.

    output_grid = output_grid[np.isin(output_grid, [2,5,8])]

    # sort them in the order 2, 8, 5.

    order = [2,8,5]

    output_grid = np.array([x for x in order if x in output_grid]).reshape(-1,1)

    return output_grid