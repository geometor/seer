"""
The transformation rule is as follows:
1. Identify all the colored objects.
2. Move the objects to the last rows, preserving the columns and putting the i-th object of color c to the row with index equal to the total number of objects of color c.
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
    
    # Create a dictionary to count and track colored cells.
    color_counts = {}
    
    # Iterate through the input grid to find single-cell objects (non-zero cells).
    for r in range(rows):
        for c in range(cols):
            color = input_grid[r, c]
            if color != 0:
                # Update color count
                if color not in color_counts:
                    color_counts[color] = [0,0] #count, row_index
                color_counts[color][0] += 1

    # Iterate through the input grid to find single-cell objects (non-zero cells).
    for r in range(rows):
        for c in range(cols):
            color = input_grid[r, c]
            if color != 0:
                # Move the object to the correct row.
                output_grid[color_counts[color][0]-1-color_counts[color][1], c] = color
                color_counts[color][1] += 1
                
    return output_grid