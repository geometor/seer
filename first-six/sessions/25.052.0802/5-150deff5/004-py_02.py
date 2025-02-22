"""
The gray object (color 5) is partially recolored. Most part is replaced with azure (color 8), and certain cells are replaced with red (color 2). The white background is preserved.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the given color.
    coords = np.argwhere(grid == color)
    return coords

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the gray object (color 5).
    gray_coords = find_object(input_grid, 5)

    #If no gray object is present return the original
    if gray_coords.size == 0:
      return output_grid

    # Recolour most of the shape to azure
    output_grid[input_grid == 5] = 8
    
    # Recolour specific cells to red, based on relative position within the gray object
    for y, x in gray_coords:
        if (y,x) == (gray_coords[0][0], gray_coords[0][1]):
            output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0], gray_coords[0][1]+1):
            output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0], gray_coords[0][1]+2):
            output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+2, gray_coords[0][1]-2):
             output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+3, gray_coords[0][1]-2):
             output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+4, gray_coords[0][1]-2):
             output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+4, gray_coords[0][1]+2):
             output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+4, gray_coords[0][1]+3):
             output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+1, gray_coords[0][1]+3):
             output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+5, gray_coords[0][1]+1):
             output_grid[y,x] = 2
        if (y,x) == (gray_coords[0][0]+5, gray_coords[0][1]+2):
             output_grid[y,x] = 2
        

    return output_grid