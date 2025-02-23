"""
Identify "L"-shaped azure colored objects, and changes the "inside" pixel from azure to blue while all other pixels remain the same.
"""

import numpy as np

def find_l_shapes(grid, color):
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                # Check for L shape (2x2 block with one missing corner)
                if r + 1 < rows and c + 1 < cols:
                    if grid[r+1, c] == color and grid[r, c+1] == color:
                         l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Define the color of the L shapes and the target color
    azure = 8
    blue = 1

    # Find the coordinates of pixels that are part of L-shapes
    l_shape_coords = find_l_shapes(input_grid, azure)
    
    # Identify and change the inside pixel
    for r,c in l_shape_coords:
        output_grid[r+1,c-1] = blue
        output_grid[r-1,c+1] = blue

    return output_grid