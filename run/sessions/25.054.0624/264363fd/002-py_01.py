"""
The transformation identifies a blue object within an azure background, traces (fully or partially) its outline with red pixels, and highlights points on the outline with green.
Original and copied objects have green highlights swapped.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all pixels of the specified color.
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None
    return coords

def get_object_bounds(coords):
    # bounding box
    min_row = np.min(coords[:, 0])
    max_row = np.max(coords[:, 0])
    min_col = np.min(coords[:, 1])
    max_col = np.max(coords[:, 1])
    return min_row, max_row, min_col, max_col

def outline_object(grid, object_coords, outline_color):
    # Create an outline of the traced object with red pixels.
    min_row, max_row, min_col, max_col = get_object_bounds(object_coords)
    output_grid = np.copy(grid)

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if grid[r,c] == grid[object_coords[0][0], object_coords[0][1]]:

                #check neighbors
                neighbors = []
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (i != 0 or j != 0):
                            neighbor_row = r + i
                            neighbor_col = c + j
                            if (0 <= neighbor_row < grid.shape[0] and 0 <= neighbor_col < grid.shape[1]):
                                  neighbors.append(grid[neighbor_row,neighbor_col])
                #if a neighbor is a different color than the object, we have an outline
                if any(neighbor != grid[object_coords[0][0], object_coords[0][1]] for neighbor in neighbors):
                    output_grid[r,c] = outline_color


    return output_grid

def find_green_highlight(grid, object_coords, highlight_color):
    # Find the green highlight within the traced object.
    min_row, max_row, min_col, max_col = get_object_bounds(object_coords)
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
             if grid[r, c] == highlight_color:
                return (r,c)
    return None

def transform(input_grid):
    # Initialize output grid with the same background color.
    output_grid = np.full(input_grid.shape, input_grid[0, 0])  # Assume background is top-left pixel

    # Find the blue object.
    blue_object_coords = find_object(input_grid, 1)

    # Trace the blue object with red.
    output_grid = outline_object(input_grid, blue_object_coords, 2)

    # find original green
    green_highlight_coords = find_green_highlight(input_grid,blue_object_coords, 3 )

    if (green_highlight_coords):
        output_grid[green_highlight_coords] = 3

    return output_grid