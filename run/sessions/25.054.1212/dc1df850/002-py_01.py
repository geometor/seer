"""
The transformation rule is as follows:
1. Identify Key Colors: Locate all pixels with the value 2 (red) in the top row.
2. Propagate Blue: For each red pixel identified in step 1, change all the white connected regions to its right and all white region below to blue (value 1). Stop when a colored block stops the spread.
3. Preserve other colors. The red and magenta pixels keep the original values.
"""

import numpy as np

def get_top_row_reds(grid):
    # find the indices of red (2) pixels in the top row
    top_row = grid[0,:]
    red_indices = np.where(top_row == 2)[0]
    return red_indices

def flood_fill_right_and_down(grid, start_x, start_y):
     #recursive flood fill to right and down, starting at start, and ending at non-white
    
    if start_x >= grid.shape[1] or start_y >= grid.shape[0] or grid[start_y, start_x] != 0:
        return grid
    
    grid[start_y, start_x] = 1
    grid = flood_fill_right_and_down(grid, start_x + 1, start_y) #right
    grid = flood_fill_right_and_down(grid, start_x, start_y+1)   #down

    return grid

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    #get the top row red pixels
    red_starts = get_top_row_reds(output_grid)

    #iterate through each and perform flood fill
    for start_x in red_starts:
       output_grid = flood_fill_right_and_down(output_grid, start_x, 0)
    
    return output_grid