"""
The transformation finds azure (8) L-shapes. For each L-shape, it identifies the vertex. It then checks the two adjacent cells (not diagonal) to the vertex that are *not* part of the L-shape. If these cells are '0', they are changed to '1' (blue). All other cells remain unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (row, col) tuples representing the vertex of each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                # Check for the four possible L-shape orientations
                if r + 1 < rows and c + 1 < cols and grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r, c))
                elif r + 1 < rows and c - 1 >= 0 and grid[r + 1, c] == color and grid[r, c - 1] == color:
                    l_shapes.append((r, c))
                elif r - 1 >= 0 and c - 1 >= 0 and grid[r - 1, c] == color and grid[r, c - 1] == color:
                    l_shapes.append((r, c))
                elif r - 1 >= 0 and c + 1 < cols and grid[r - 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append((r, c))
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find L-shapes of color 8 (azure)
    l_shapes = find_l_shapes(output_grid, 8)

    # Change the color of the adjacent cells to the vertex to 1 (blue)
    for r, c in l_shapes:
        # Get the adjacent cells
        adjacent_cells = []
        if r + 1 < rows:
            adjacent_cells.append((r + 1, c))
        if r - 1 >= 0:
            adjacent_cells.append((r - 1, c))
        if c + 1 < cols:
            adjacent_cells.append((r, c + 1))
        if c - 1 >= 0:
            adjacent_cells.append((r, c - 1))

        # Filter out cells that are part of the L-shape
        for ar, ac in adjacent_cells:
            is_part_of_l_shape = False
            for lr, lc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= lr < rows and 0 <= lc < cols and (lr, lc) != (r, c) and (lr, lc) == (ar, ac) and output_grid[lr,lc] == 8:
                    is_part_of_l_shape = True
                    break
            
            #if cell is 0 and not part of the L shape:
            if not is_part_of_l_shape and output_grid[ar,ac] == 0:
                output_grid[ar, ac] = 1
                    

    return output_grid