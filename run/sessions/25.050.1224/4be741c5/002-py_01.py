"""
The transformation rule identifies distinct colored regions in the input grid and represents each with a single cell in the output grid. The output is a 1x3 grid with cells ordered by color code: yellow (4), red (2), and azure (8).
"""

import numpy as np

def get_distinct_colors(grid):
    """
    Returns a sorted list of distinct colors present in the grid.
    """
    return sorted(np.unique(grid).tolist())

def transform(input_grid):
    """
    Transforms the input grid into a 1x3 grid representing the distinct colors.
    """
    # Get the distinct colors from the input grid
    distinct_colors = get_distinct_colors(input_grid)

    #Initialize the output grid as 1xN array,
    #with N being the number of unique colors.
    
    output_grid = np.array(distinct_colors).reshape(1,-1)

    # remove all colors different than 2, 4 and 8.
    
    output_grid = output_grid[np.isin(output_grid, [2,4,8])]
    
    # sort them in the order 4, 2, 8.
    
    order = [4,2,8]
    
    output_grid = np.array([x for x in order if x in output_grid]).reshape(1,-1)    
    
    return output_grid