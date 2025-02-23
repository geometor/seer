"""
The program identifies "L"-shaped objects formed by azure (8) pixels and adds a blue (1) pixel at the interior corner of each L. An "L" shape is a 2x2 block of azure pixels with one pixel missing. The rest of the grid remains unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds the coordinates of the interior corner of L-shaped objects of the specified color.
    Correctly handles all four orientations of the L.
    """
    coords = []
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            block = grid[i:i+2, j:j+2]
            if np.sum(block == color) == 3:  # Check for exactly three cells of the target color
                # Find the missing corner (the cell that's not the target color)
                if block[0, 0] != color:
                    coords.append((i, j))
                elif block[0, 1] != color:
                    coords.append((i, j+1))
                elif block[1, 0] != color:
                    coords.append((i+1, j))
                elif block[1, 1] != color:
                    coords.append((i+1, j+1))
    return coords

def transform(input_grid):
    """
    Transforms the input grid by adding a blue (1) pixel inside the corner of each azure (8) L-shaped object.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input

    # Find the coordinates of the corners of L-shaped azure objects
    l_shape_corners = find_l_shapes(output_grid, 8)

    # Add a blue pixel (1) at the corner of each L-shaped object
    for corner in l_shape_corners:
        output_grid[corner] = 1  # Fill the corner with blue

    return output_grid