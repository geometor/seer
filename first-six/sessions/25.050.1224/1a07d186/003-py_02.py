import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    The transformation rule is as follows:
    1.  Two main persistent objects, red and blue, mostly keep the same properties.
    2.  Move up by one row those objects.
    3.  Single cells by color:
        *   Single red cells (color 2) which are not on the same row of the red line are moved to the upper row or down row.
        *   Single blue cells (color 1) which are not on the same row of the blue line are moved to the row below.
        *   Delete any single cell not being object 1 or object 2.
    """
    output_grid = np.zeros_like(input_grid)
    red_line_row = -1
    blue_line_row = -1
    
    # Find the row indices of the red and blue lines
    for r in range(input_grid.shape[0]):
        if all(input_grid[r, :] == 2):
            red_line_row = r
        elif all(input_grid[r, :] == 1):
            blue_line_row = r

    # Move and preserve red and blue horizontal lines by one row
    if red_line_row != -1:
        output_grid[red_line_row -1, :] = 2
    if blue_line_row != -1:
        output_grid[blue_line_row - 1, :] = 1

    # Iterate through input cells and apply actions
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] == 2 and r != red_line_row:
                if red_line_row !=-1:
                    if r < red_line_row:
                      output_grid[red_line_row-2,c]=2
                    else:
                      output_grid[red_line_row,c]=2
            elif input_grid[r, c] == 1 and r != blue_line_row and blue_line_row!=-1 :
                 output_grid[blue_line_row, c] = 1

    return output_grid