"""
The transformation rule is as follows: Find the top-left most and bottom-right most azure (8) objects. The top-left most is the object that has the smallest x and y coordinates. The bottom-right most has the largest x and y coordinates.
Create a blue pixel (1) by moving +1 on the y-axis from the top-left most, and another by moving -1 in the x-axis of the bottom-right most azure pixel. The rest of azure color pixels remain unchanged.
"""

import numpy as np

def find_azure_objects(grid):
    # Find coordinates of all azure (8) pixels.
    azure_coords = np.argwhere(grid == 8)
    return azure_coords

def find_top_leftmost(coords):
    # Find the top-leftmost azure pixel.
    min_row = np.min(coords[:, 0])
    min_col_candidates = coords[coords[:,0] == min_row]
    min_col = np.min(min_col_candidates[:,1])
    
    return (min_row,min_col)
    

def find_bottom_rightmost(coords):
    # Find the bottom-rightmost azure pixel.

    max_row = np.max(coords[:, 0])
    max_col_candidates = coords[coords[:,0] == max_row]
    max_col = np.max(max_col_candidates[:,1])

    return (max_row, max_col)
    

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Find all azure objects.
    azure_coords = find_azure_objects(input_grid)

    if len(azure_coords) >0:
        # Find the top-leftmost and bottom-rightmost azure pixels.
        top_leftmost = find_top_leftmost(azure_coords)
        bottom_rightmost = find_bottom_rightmost(azure_coords)

        # Create blue pixels based on the top-leftmost and bottom-rightmost azure pixels.
        output_grid[top_leftmost[0], top_leftmost[1] + 1] = 1  # +1 on the y-axis
        output_grid[bottom_rightmost[0] - 1, bottom_rightmost[1]] = 1  # -1 on the x-axis

    return output_grid