"""
1.  **Expand the grid:** Double the dimensions of the input grid to create the output grid.
2.  **Copy and Extend Grey:** all grey object in input are present in the output. Add azure next to each grey, expanding a copy of the grey objects to the border.
3. **Border Exception:** azure pixels should always be present at the border, so no need to extend the border.
"""

import numpy as np

def get_gray_pixels(grid):
    # Find coordinates of gray (5) pixels.
    return np.argwhere(grid == 5)

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height, output_width = 2 * input_height, 2 * input_width
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Find gray pixels in the input grid.
    gray_pixels = get_gray_pixels(input_grid)

    # Double the coordinates for the expanded grid.
    for r, c in gray_pixels:
      output_grid[r*2, c*2] = 5

    #fill corners
    for r,c in gray_pixels:
        output_grid[r*2, c*2] = 5
        
        #expand the grid
        if r*2 == 0:
            output_grid[r*2+1,c*2] = 8 #one bellow
            #fill corners
            output_grid[r*2,:] = 8 #fill top row
            output_grid[r*2+1,0:c*2] = 8 #one bellow top corner
        elif r*2 == output_height-2:
            output_grid[r*2-1,c*2] = 8 #one above
            #fill corners
            output_grid[r*2+1,:] = 8 #fill botton row
            output_grid[r*2,0:c*2] = 8 #one above top corner
        else:
            output_grid[r*2-1,c*2] = 8 #one above
            output_grid[r*2+1,c*2] = 8 #one bellow

        if c*2 == 0:
            output_grid[r*2,c*2+1] = 8 #one right
            #fill corners
            output_grid[:,c*2] = 8 #fill left column
            output_grid[0:r*2,c*2+1] = 8 #one right left corner
        elif c*2 == output_width -2:
            output_grid[r*2,c*2-1] = 8 #one left
            #fill corners
            output_grid[:,c*2+1] = 8 #fill right column
            output_grid[0:r*2,c*2] = 8 #one left to corner
        else:
            output_grid[r*2,c*2+1] = 8 #one right
            output_grid[r*2,c*2-1] = 8 #one left

    return output_grid