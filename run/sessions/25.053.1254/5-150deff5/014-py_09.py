"""
Identifies contiguous shapes of gray (5) pixels in the input grid and replaces these pixels with azure (8) and red (2) in the output grid. Red pixels form the outer "edge" of the shape, and azure pixels fill the interior. Edge pixels are adjacent to empty (0) pixels or the border of the input.
"""

import numpy as np

def get_contiguous_shape(grid, color):
    """
    Finds a contiguous shape of a given color in a grid.
    """
    coords = np.argwhere(grid == color)
    if len(coords) == 0:
        return []

    shape = [tuple(coords[0])]
    remaining_coords = set(map(tuple, coords[1:]))

    i = 0
    while i < len(shape):
        current_coord = shape[i]
        neighbors_to_add = []
        for neighbor in remaining_coords:
            diff = np.abs(np.array(current_coord) - np.array(neighbor))
            if np.sum(diff) == 1:  # Check for adjacency (Manhattan distance of 1)
                neighbors_to_add.append(neighbor)

        for neighbor in neighbors_to_add:
            shape.append(neighbor)
            remaining_coords.remove(neighbor)
        i += 1

    return shape

def is_edge_pixel(grid, coord, shape_coords):
    """
    Checks if a pixel is an edge pixel within a contiguous shape.  A pixel
    is an edge if at least one of its N, S, E, or W neighbors is a 0 *or*
    is outside the grid
    """
    r, c = coord
    neighbors = [
        (r - 1, c),  # North
        (r + 1, c),  # South
        (r, c - 1),  # West
        (r, c + 1),  # East
    ]

    for nr, nc in neighbors:
        if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
            if grid[nr, nc] == 0: #check if neighbor is empty
                return True
        else:
            return True # Found a neighbor outside the image

    return False  # All valid neighbors are within the shape and not 0


def transform(input_grid):
    """
    Transforms the input grid by replacing gray shapes with red and azure.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    shape_color = 5  # Gray
    shape_coords = get_contiguous_shape(input_grid, shape_color)
    shape_coords_set = set(shape_coords) #for faster lookup in is_edge_pixel

    if not shape_coords:
        return output_grid.tolist()

    # Iterate through the shape and apply the transformation.
    for r, c in shape_coords:
        if is_edge_pixel(input_grid, (r, c), shape_coords_set):
            output_grid[r, c] = 2  # Red
        else:
            output_grid[r, c] = 8  # Azure

    return output_grid.tolist()