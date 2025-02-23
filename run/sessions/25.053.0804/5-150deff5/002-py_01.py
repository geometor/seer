"""
1.  **Identify the Gray Object:** Locate the contiguous block of gray (5) pixels in the input grid.
2.  **Split and recolor:**
    *   The gray pixels in the top two rows that are part of the gray object, change them to azure (8).
    *   From the third row down, find pixels that have a gray pixel directly above them, change them to azure(8).
    *   Change all of the remaining gray pixels to red (2).
"""

import numpy as np

def get_object_coordinates(grid, color):
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    
    # find gray object
    gray_coords = get_object_coordinates(input_grid, 5)
    
    # change to azure (8) in top two rows
    for r, c in gray_coords:
        if r <= 2:
            output_grid[r, c] = 8
        
    # check from row 3 and change gray pixel to azure if there's a gray above
    for r, c in gray_coords:      
        if r > 2:
            if (r-1,c) in gray_coords and input_grid[r-1,c] == 5:
                output_grid[r,c] = 8
                
    # change remainig to red
    for r, c in gray_coords:
        if output_grid[r,c] == 5:
            output_grid[r, c] = 2

    return output_grid