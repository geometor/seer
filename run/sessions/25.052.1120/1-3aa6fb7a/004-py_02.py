"""
1.  **Identify L-shaped objects:** Find all L-shaped objects of color 8 (azure) in the input grid. An L-shape is defined as three connected cells of color 8 where two cells are adjacent in a row or column, and the third cell is adjacent to one of those two, forming a 2x2 square with one cell missing.

2.  **Locate the Inner Corner:** For each identified L-shape, determine the "inner corner." The inner corner is the cell *adjacent* to the 'tip' of the L and that would complete a 2x2 square. This cell is always adjacent (horizontally or vertically) to two cells of the L-shape. It never touches the tip diagonally.

3. **Insert Blue Cell**: Change color of inner corner to 1(blue).
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of coordinates (row, col) of the "tip" of each L.
    The tip is defined as the cell which has neighbors to the right and down.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L-shape (tip at top-left)
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r, c))
                # Check for L-shape (tip at top-right)
                elif grid[r + 1, c] == color and grid[r, c-1] == color and c > 0:
                    l_shapes.append((r,c))
                # Check for L-shape (tip at bottom-left)
                elif grid[r-1,c] == color and grid[r,c+1] == color and r > 0:
                    l_shapes.append((r,c))
                 # Check for L-shape (tip at bottom-right)
                elif grid[r-1,c] == color and grid[r,c-1] == color and r > 0 and c > 0:
                    l_shapes.append((r,c))    
    return l_shapes

def get_inner_corner(grid, tip, color):
    """
    Finds the inner corner coordinate for a given L-shape tip.
    """
    r, c = tip
    # Check which type of L-shape it is and calculate the inner corner
    
    if grid[r + 1, c] == color and grid[r, c + 1] == color:
         return (r + 1, c + 1)

    elif grid[r + 1, c] == color and grid[r, c - 1] == color:
        return (r+1, c-1)
        
    elif grid[r - 1, c] == color and grid[r, c + 1] == color:
        return (r-1, c+1)
        
    elif grid[r - 1, c] == color and grid[r, c - 1] == color:
        return (r-1,c-1)

    return None  # Should not happen if the tip is correctly identified


def transform(input_grid):
    """
    Transforms the input grid according to the L-shape rule.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all L-shapes of color 8
    l_shapes = find_l_shapes(input_grid, 8) # use input_grid

    # For each L-shape, find the inner corner and change its color to 1
    for tip in l_shapes:
        inner_corner = get_inner_corner(input_grid, tip, 8) # use input_grid
        if inner_corner:
            output_grid[inner_corner] = 1

    return output_grid