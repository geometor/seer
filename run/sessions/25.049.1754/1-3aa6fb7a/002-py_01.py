"""
Transformation Rule:

Identify azure (color 8) objects that form an L-shape using three pixels. 
For the single azure pixel that defines the L, check its row:
- If it is in the second row, replace the white pixel on its right with a blue pixel (color 1).
- If it is in the fifth row, replace the white pixel on its left with a blue pixel (color 1).
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specified color and returns the coordinates of the single pixel.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for 2x2 blocks to identify potential L-shapes
            block = grid[r:r+2, c:c+2]
            if np.sum(block == color) == 3:
                # Determine the single pixel's coordinates
                if block[0, 0] == color and block[0, 1] == color and block[1, 0] == color:
                    l_shapes.append((r+1,c+1))
                elif block[0,0] == color and block[0,1] == color and block[1,1] == color:
                    l_shapes.append((r+1,c))
                elif block[0,0] == color and block[1,0] == color and block[1,1] == color:
                    l_shapes.append((r,c+1))
                elif block[0,1] == color and block[1,0] == color and block[1,1] == color:
                    l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    # Iterate through the found L-shapes and modify the output grid
    for r, c in l_shapes:
        if r == 1:  # Second row (adjust for 0-indexing)
            if c + 1 < output_grid.shape[1]:
                output_grid[r, c + 1] = 1
        elif r == 4:  # Fifth row (adjust for 0-indexing)
            if c - 1 >= 0:
                output_grid[r, c - 1] = 1

    return output_grid