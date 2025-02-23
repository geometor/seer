"""
The transformation rule is as follows:
1. Identify single-cell objects of colors other than 0 in the input grid.
2. Move all identified objects to the last row of the grid, maintaining their column positions.
3. All other cells in the grid, not occupied by the moved objects, are set to 0.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize the output grid as a copy of the input grid, then set everything to 0.
    output_grid = np.zeros_like(input_grid)
    
    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape
    
    # Iterate through the input grid to find single-cell objects (non-zero cells).
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                # Move the object to the last row, keeping the same column.
                output_grid[rows - 1, c] = input_grid[r, c]
                
    return output_grid