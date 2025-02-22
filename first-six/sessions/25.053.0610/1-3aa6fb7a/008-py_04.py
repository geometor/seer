"""
The transformation identifies all "L"-shaped azure objects in the input grid. 
For each "L" shape, the inside corner pixel is changed to blue (value 1).
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (corner_row, corner_col) tuples for each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L shape (2x2 block with one missing corner)
                neighbors = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                color_count = sum(1 for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color)
                if color_count == 2:
                    l_shapes.append((r, c))
    return l_shapes

def get_inside_corner(grid, corner_row, corner_col):
    """
    Determines the inside corner coordinates of an L-shape given its corner pixel.
    """
    rows, cols = grid.shape

    # Check orientation and determine inside corner
    if corner_row == 0: # Top row
        return corner_row + 1, corner_col
    elif corner_col == 0: # Left column
        return corner_row , corner_col + 1
    else:  # other rows
        return corner_row + 1, corner_col + 1

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the L-shaped objects of color azure (8)
    l_shapes = find_l_shapes(input_grid, 8)
    
    # Change inside corner of each L-shape to blue
    for corner_row, corner_col in l_shapes:
        inside_row, inside_col = get_inside_corner(input_grid, corner_row, corner_col)
        output_grid[inside_row, inside_col] = 1

    return output_grid