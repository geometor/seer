"""
The transformation rule is: Find the azure (8) colored L-shapes. For any azure L-shape, change the "empty" cell to its right (specifically, the cell to the right of the "L"'s vertex) to color blue (1). If a cell is not subject to modification according to this rule, it is left unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (row, col) tuples representing the vertex of each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for the four possible L-shape orientations
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r, c))
                elif grid[r + 1, c] == color and grid[r, c - 1] == color:
                    l_shapes.append((r,c))
                elif grid[r - 1, c] == color and grid[r, c - 1] == color:
                    l_shapes.append((r,c))
                elif grid[r - 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find L-shapes of color 8 (azure)
    l_shapes = find_l_shapes(output_grid, 8)

    # Change the color of the cell to the right of the vertex to 1 (blue)
    for r, c in l_shapes:

        if output_grid[r,c] == output_grid[r+1,c] == output_grid[r,c+1] and c + 2 < cols:
            if output_grid[r,c+2] == 0: output_grid[r, c + 2] = 1
        
        if output_grid[r,c] == output_grid[r+1,c] == output_grid[r,c-1] and c -2 >= 0:
            if output_grid[r,c-2] == 0 : output_grid[r,c-2] = 0

        if output_grid[r,c] == output_grid[r-1,c] == output_grid[r,c+1] and c + 2 < cols:
            if output_grid[r,c+2] == 0: output_grid[r, c + 2] = 1
                
        if output_grid[r,c] == output_grid[r-1,c] == output_grid[r,c-1] and c - 2 >= 0:
            if output_grid[r,c-2] == 0: output_grid[r, c-2] = 0

    return output_grid