"""
The transformation involves identifying three 2x1 rectangles (blue, red, and yellow) in the input grid and repositioning them vertically. The blue rectangle stays in place, the red rectangle moves down one row, and the yellow rectangle moves up one row. This results in all three rectangles being aligned in the third and fourth rows of the output grid, maintaining their original column positions.
"""

import numpy as np

def find_objects_2x1(grid):
    """Finds 2x1 rectangle objects in the grid."""
    objects = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            rectangle = grid[r:r+2, c:c+1]
            if np.all(rectangle == rectangle[0,0]) and rectangle[0,0] != 0:
                objects.append({'color': rectangle[0,0], 'position': (r, c)})
    return objects

def transform(input_grid):
    """
    Transforms the input grid by moving the 2x1 rectangles.
    """
    # Initialize output grid as a zero array with the same shape as the input
    output_grid = np.zeros_like(input_grid)

    # Find the 2x1 rectangle objects
    objects = find_objects_2x1(input_grid)
    
    #Move each object according to the observed rule
    for obj in objects:
        color = obj['color']
        r, c = obj['position']
        
        if color==1: #blue
            new_row = 2
        elif color == 2: #red
            new_row = 2
        elif color == 4: # yellow
            new_row = 2
            
        output_grid[new_row:new_row+2, c:c+1] = color
    return output_grid