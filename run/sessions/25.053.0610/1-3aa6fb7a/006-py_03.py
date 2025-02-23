"""
The transformation identifies all "L"-shaped azure objects in the input grid. 
An "L" shape is defined as a 2x2 block where three of the four pixels are azure (value 8).
The inside corner pixel of each "L" shape, which is the pixel within the 2x2 block that is *not* azure, is changed to blue (value 1).
All other pixels remain unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (inside_corner_row, inside_corner_col) tuples for each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for 2x2 block
            block = grid[r:r+2, c:c+2]
            if np.sum(block == color) == 3:
                # Find the inside corner (the non-color pixel within the 2x2 block)
                for i in range(2):
                    for j in range(2):
                        if block[i, j] != color:
                            inside_corner_row = r + i
                            inside_corner_col = c + j
                            l_shapes.append((inside_corner_row, inside_corner_col))
    return l_shapes

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the L-shaped objects of color azure (8)
    l_shapes = find_l_shapes(input_grid, 8)
    
    # Iterate through all found L-shapes and change the inside corner to blue
    for inside_corner_row, inside_corner_col in l_shapes:
        output_grid[inside_corner_row, inside_corner_col] = 1

    return output_grid