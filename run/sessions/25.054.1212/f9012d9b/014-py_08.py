"""
The program identifies two 2x2 regions within the input grid: the top-left 2x2 region, and the 2x2 top right most gray regions.
If gray is identified in top left 2x2 area, fill output grid with gray. Fill output grid bottom right with color of top right corner input.
"""

import numpy as np

def get_top_left_2x2(grid):
    """Extracts the top-left 2x2 subgrid."""
    return grid[0:2, 0:2]

def get_top_rightmost_gray_2x2(grid):
    """Finds the top-rightmost 2x2 region of solid gray (5)."""
    height, width = grid.shape
    for r in range(height - 1):
        for c in range(width - 1):
            subgrid = grid[r:r+2, c:c+2]
            if np.all(subgrid == 5):
                return r,c
    return None, None

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""

    # Initialize the output grid as 2x2, filled with a default value (e.g., 0).
    output_grid = np.zeros((2, 2), dtype=int)

    # Get the top-left 2x2 subgrid.
    top_left_2x2 = get_top_left_2x2(input_grid)
    
    # fill output with gray (5)
    output_grid[:] = 5

    # Get the top right element color.
    top_right_color = input_grid[0,0]
    
    output_grid[1,1] = top_right_color


    return output_grid