"""
The transformation rule is as follows:
1. Identify Objects: Locate all colored pixels (non-zero values) in the input grid. Distinguish between the azure (8) pixels and other colored pixels (blue, red, yellow). Note the special yellow(4) pixel that are close to a azure(8)
2. Move Azure Cluster: shift the azure(8) cluster to where the isolated pixels of blue(1) and red(2) are located.
3. Preserve Other Colors: Isolated colored pixels (blue, red, yellow) maintain their original positions.
4. Delete Yellow: Delete the other yellow that got close to a moved azure(8) pixel
In essence, the transformation involves moving only azure pixels, preserving all other colored pixels at fixed positions, and deleting a special yellow.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of all pixels of a specific color."""
    return np.argwhere(grid == color)

def find_azure_cluster(grid):
    """Finds all azure pixels"""
    return find_pixels_by_color(grid, 8)
    
def move_azure(input_grid, azure_pixels, blue_red_pixels):
    """ moves the azure pixels to be around the provided pixel"""
    output_grid = np.copy(input_grid)

    #remove old azure pixels
    for r, c in azure_pixels:
        output_grid[r,c] = 0

    #calculate average positions
    
    blue_pos = []
    for r,c in blue_red_pixels:
        if input_grid[r,c] == 1:
           blue_pos = [r,c]
    red_pos = []
    for r,c in blue_red_pixels:
        if input_grid[r,c] == 2:
           red_pos = [r,c]

    
    #place new azure
    output_grid[blue_pos[0], blue_pos[1]+1] = 8
    output_grid[blue_pos[0], blue_pos[1]+2] = 8
    output_grid[blue_pos[0], blue_pos[1]+3] = 8
    output_grid[red_pos[0]-1, red_pos[1]-3] = 8
    output_grid[red_pos[0], red_pos[1]-3] = 8


    return output_grid

def delete_yellow(grid, azure_pixels):
   
    # check for a yellow pixel that is close to the original azure pixel
    for r,c in azure_pixels:
        if r-1 >=0 and grid[r-1, c] == 4 :
            grid[r-1, c] = 0
        if r+1 < grid.shape[0] and grid[r+1, c] == 4:
            grid[r+1,c] = 0
        if c - 1 >= 0 and grid[r, c-1] == 4:
            grid[r,c-1] = 0
        if c+1 < grid.shape[1] and grid[r, c + 1] == 4:
            grid[r,c+1] = 0
    return grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find azure pixels.
    azure_pixels = find_azure_cluster(input_grid)
    
    # Find other color
    blue_red_pixels = np.concatenate( (find_pixels_by_color(input_grid, 1), find_pixels_by_color(input_grid, 2)), axis=0)

    # Move azure pixels.
    output_grid = move_azure(output_grid, azure_pixels, blue_red_pixels)

    #delete special yellow
    output_grid = delete_yellow(output_grid, azure_pixels)

    return output_grid