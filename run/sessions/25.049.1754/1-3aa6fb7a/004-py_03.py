"""
Transformation Rule:

Identify azure (color 8) objects forming an L-shape (3 pixels).
For each L-shape, find the single pixel not part of the 2x1 block.
Based on this pixel's row:
- Row 1 (2nd row): Place blue (1) pixel to the left.
- Row 2 (3rd row): Place blue (1) pixel to the right.
- Row 4 (5th row): Place blue (1) pixel to the left.
- Row 5 (6th row): Place blue (1) pixel to the left.
Handle edge cases (grid boundaries).
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specified color and returns the coordinates
    of the single pixel that's not part of the 2x1 block.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for 2x2 blocks
            block = grid[r:r+2, c:c+2]
            if np.sum(block == color) == 3:
                # Determine the single pixel's coordinates
                if block[0, 0] == color and block[0, 1] == color and block[1, 0] == color:
                    l_shapes.append((r+1, c+1))  # Bottom-right
                elif block[0, 0] == color and block[0, 1] == color and block[1, 1] == color:
                    l_shapes.append((r+1, c))    # Bottom-left
                elif block[0, 0] == color and block[1, 0] == color and block[1, 1] == color:
                    l_shapes.append((r, c+1))    # Top-right
                elif block[0, 1] == color and block[1, 0] == color and block[1, 1] == color:
                    l_shapes.append((r, c))      # Top-left
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid based on the L-shape rule.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    for r, c in l_shapes:
        if r == 1:  # Second row
            if c - 1 >= 0:
                output_grid[r, c - 1] = 1
        elif r == 2:  # Third row
            if c + 1 < output_grid.shape[1]:
                output_grid[r, c + 1] = 1
        elif r == 4 or r == 5: #Fifth and sixth row
            if c - 1 >= 0:
                output_grid[r,c-1] = 1


    return output_grid