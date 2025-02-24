"""
1.  **Identify Non-Blue Elements:** Focus on the non-blue (non-1) colored pixels in the input grid.
2.  **Extract Sub-grid:** From the top-left corner of the first identified non-blue pixel (reading row first) extract non-blue pixels to a 3 x 3 output grid.
3.  **Handle edges:** If there are not enough pixels to fill a row or column use 0s.
"""

import numpy as np

def get_non_blue_pixels(grid):
    """
    returns an array of (r,c) tuples of indexes of all non-blue pixels
    """
    coords = []
    rows, cols = np.shape(grid)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]!=1:
                coords.append((r,c))
    return coords

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # find non-blue pixels
    non_blue_pixels = get_non_blue_pixels(input_grid)
    
    # check we have some
    if len(non_blue_pixels)==0:
        return output_grid # blank

    # start populating the output grid
    start_row, start_col = non_blue_pixels[0]
    
    for out_row in range(3):
        for out_col in range(3):
            in_row = start_row + out_row
            in_col = start_col + out_col
            
            # bounds check - could use a try-except as alternative
            if in_row < len(input_grid) and in_col < len(input_grid[0]):
                if input_grid[in_row][in_col]!=1:
                    output_grid[out_row][out_col]= input_grid[in_row][in_col]
                # else 0 already there

    return output_grid