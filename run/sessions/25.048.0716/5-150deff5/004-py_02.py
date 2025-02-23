"""
The transformation involves finding the shape formed by color 5, replacing the outer layer with color 8, and replacing the rest with color 2.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the specified color.
    coords = np.argwhere(grid == color)
    return coords

def get_neighbors(grid, coord):
    # Get the neighbors of a given coordinate, including diagonals.
    rows, cols = grid.shape
    r, c = coord
    neighbors = []
    for i in range(max(0, r-1), min(rows, r+2)):
        for j in range(max(0, c-1), min(cols, c+2)):
            if (i, j) != (r, c):
                neighbors.append((i, j))
    return neighbors

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    
    # Find the object with color 5.
    object_coords = find_object(input_grid, 5)
    
    # If no object of color 5 is found, return input grid
    if len(object_coords) == 0:
        return output_grid

    # Find the outer layer (border) of the object.
    border_coords = []
    inner_coords = []
    for coord in object_coords:
        neighbors = get_neighbors(input_grid, coord)
        is_border = False
        for neighbor in neighbors:
            if input_grid[neighbor] != 5:
                is_border = True
                break
        if is_border:
            border_coords.append(coord)
        else:
            inner_coords.append(coord)

    # Change the color of the border cells to 8.
    for coord in border_coords:
        output_grid[coord] = 8
        
    # Change the color of inner cells to 2
    for coord in inner_coords:
        output_grid[coord] = 2

    return output_grid