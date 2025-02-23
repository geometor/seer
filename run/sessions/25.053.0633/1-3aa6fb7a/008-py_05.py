"""
Identify "L"-shaped azure colored objects, and changes the "inside" pixel from azure to blue while all other pixels remain the same.
"""

import numpy as np

def is_l_shape(grid, r, c, color):
    """Checks if the cell at (r, c) is part of an L-shape of the given color."""
    if grid[r, c] != color:
        return False

    rows, cols = grid.shape
    count = 0
    neighbors = []

    # Check adjacent cells
    if r > 0 and grid[r-1, c] == color:
        count += 1
        neighbors.append((r - 1, c))
    if r < rows - 1 and grid[r+1, c] == color:
        count += 1
        neighbors.append((r + 1, c))
    if c > 0 and grid[r, c-1] == color:
        count += 1
        neighbors.append((r, c - 1))
    if c < cols - 1 and grid[r, c+1] == color:
        count += 1
        neighbors.append((r, c + 1))

    # Check if it forms an L-shape (exactly two neighbors that are either both horizontal or both vertical)
    if count == 2:
        if neighbors[0][0] == neighbors[1][0] or neighbors[0][1] == neighbors[1][1]:  # Check rows or cols
            return True

    return False
    
def find_l_shapes(grid, color):
    """Finds all pixels that are part of L-shapes of a given color."""
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if is_l_shape(grid, r, c, color):
               l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    """Transforms the input grid according to the L-shape rule."""
    output_grid = np.copy(input_grid)
    azure = 8
    blue = 1

    l_shape_coords = find_l_shapes(input_grid, azure)
    
    
    rows, cols = input_grid.shape

    for r, c in l_shape_coords:
       # Check adjacent cells for the 'inside' pixel to turn blue
        if r > 0 and r+1 < rows and input_grid[r-1,c] == azure and input_grid[r+1,c] == azure:
             output_grid[r,c] = blue
        elif c > 0 and c+1 < cols and input_grid[r,c-1] == azure and input_grid[r,c+1] == azure:
             output_grid[r,c] = blue        

    return output_grid