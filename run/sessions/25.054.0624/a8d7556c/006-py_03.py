"""
Identifies a shape made of white (0) pixels within a gray (5) background. 
It then "fills" the gray area directly adjacent to the shape, both inside and outside, 
changing those gray pixels to red (2). The original shape and grid dimensions are preserved.  
Adjacency includes diagonal connections. The fill does NOT propagate beyond directly adjacent pixels.
"""

import numpy as np

def find_shape(grid, shape_color=0):
    # Find coordinates of pixels belonging to the shape
    shape_coords = np.argwhere(grid == shape_color)
    return shape_coords

def get_adjacent_pixels(grid, shape_coords, fill_color=5):
    rows, cols = grid.shape
    adjacent_coords = set()

    for r, c in shape_coords:
        # Check all 8 neighbors (including diagonals)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Skip the cell itself
                nr, nc = r + i, c + j
                # Check boundaries and if the neighbor is a gray pixel
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == fill_color:
                    adjacent_coords.add((nr, nc))
    return list(adjacent_coords)

def transform(input_grid):
    """
    Transforms the input grid by filling gray areas adjacent to white shapes with red.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the coordinates of the white shape (white pixels)
    shape_coords = find_shape(output_grid, shape_color=0)

    # Get coordinates of gray pixels directly adjacent to the shape (including diagonals)
    adjacent_to_fill = get_adjacent_pixels(output_grid, shape_coords, fill_color=5)

    # Fill the identified adjacent pixels with red (2), preserving original white pixels
    for r, c in adjacent_to_fill:
        output_grid[r, c] = 2  # Fill with red

    return output_grid