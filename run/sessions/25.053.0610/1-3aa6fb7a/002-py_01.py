"""
The transformation identifies two "L"-shaped azure objects in the input grid. The top-left "L" shape remains unchanged. 
The bottom-right "L" shape has its corner pixel changed to blue (value 1).
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

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the L-shaped objects of color azure (8)
    l_shapes = find_l_shapes(input_grid, 8)
    
    # Find corner for color change
    if len(l_shapes) > 1:
        # Identify corner of the L-shape
        
        # Find the bottom-right L-shape
        max_row = -1
        bottom_right_l = None
        for r,c in l_shapes:
          if r >= max_row:
            max_row = r
            bottom_right_l = (r,c)

        # find the coordinates of the inside corner and make it blue
        corner_row, corner_col = bottom_right_l
        output_grid[corner_row+1, corner_col+1] = 1

    return output_grid