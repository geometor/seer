"""
For each azure L-shape in the input grid:
Find its uppermost and leftmost cell. Check the shape to determine if we should paint the cell down, right or up of the top-left corner.
If the shape is vertical paint in blue (color 1) down.
If the shape is horizontal paint in blue (color 1) right.
"""

import numpy as np

def find_l_shapes(grid, color):
    # Find all L-shaped objects of a specific color in the grid.
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L-shape (3 cells)
                if grid[r + 1, c] == color and grid[r, c + 1] == color :
                    l_shapes.append((r, c))
                elif grid[r+1,c] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))
                elif grid[r,c+1] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))
                elif grid[r,c-1] == color and grid[r+1,c-1] == color:
                    l_shapes.append((r,c))


    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each azure L-shape object, change the color of the cell to the immediate right
    of its top-left corner to blue.
    """
    output_grid = np.copy(input_grid)
    azure_l_shapes = find_l_shapes(output_grid, 8)

    for r, c in azure_l_shapes:
        #Check the shape of each L
        if output_grid[r + 1, c] == 8 and output_grid[r, c + 1] == 8 :
           # Change the cell to the right of the top-left corner to blue
           if c + 1 < output_grid.shape[1]:
              output_grid[r, c + 1] = 1
        elif output_grid[r+1,c] == 8 and output_grid[r+1,c+1] == 8:
             if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c] = 1
        elif output_grid[r,c+1] == 8 and output_grid[r+1,c+1] == 8:
            if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c] = 1
        elif  output_grid[r,c-1] == 8 and output_grid[r+1,c-1] == 8:
           if c - 1 < output_grid.shape[1] and c > 0:
              output_grid[r, c - 1] = 1
    return output_grid