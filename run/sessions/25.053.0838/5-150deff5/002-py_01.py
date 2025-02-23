"""
1. Identify the connected component of gray pixels.
2. Peel - find the set of pixels that have non-gray neighbors
3. Recolor the peeled pixels to azure
4. Recolor the remaining pixels to red
"""

import numpy as np

def get_object_pixels(grid, color):
    return np.argwhere(grid == color)

def get_neighbors(grid, row, col):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                neighbors.append((nr, nc))
    return neighbors

def peel(grid, object_pixels):
    peeled_pixels = []
    remaining_pixels = []
    
    object_pixels_set = set(map(tuple, object_pixels)) # convert to set of tuples

    for row, col in object_pixels_set:
        neighbors = get_neighbors(grid, row, col)
        is_peeled = False
        for nr, nc in neighbors:
            if (nr, nc) not in object_pixels_set:
                is_peeled = True
                break
        if is_peeled:
            peeled_pixels.append((row, col))
        else:
            remaining_pixels.append((row, col))
    return peeled_pixels, remaining_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Identify object pixels
    gray_pixels = get_object_pixels(input_grid, 5)

    # Peel the object
    peeled_pixels, remaining_pixels = peel(input_grid, gray_pixels)

    # Recolor peeled pixels to azure (8)
    for row, col in peeled_pixels:
        output_grid[row, col] = 8
        
    # Recolor the rest of the pixels to red
    for row, col in remaining_pixels:
      output_grid[row, col] = 2

    return output_grid