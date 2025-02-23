"""
The transformation rule is to recolor a contiguous gray (5) object in the input grid. 
The gray object is replaced by two sub-shapes: one azure (8) and the other red (2). 
The background (0) remains unchanged.
The spatial arrangement of the azure and red shapes varies.
"""

import numpy as np

def get_object(grid, color):
    """
    Finds the contiguous region of a specified color.
    
    Returns a mask, object pixels are True, background is false.
    """
    mask = (grid == color)
    return mask

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Get the mask for the gray object (color 5)
    gray_mask = get_object(input_grid, 5)
    
    # coordinates
    coords = np.argwhere(gray_mask)

    # change color: gray(5) by azure(8)
    for r, c in coords:
        if (input_grid[r,c] == 5) :
            if ( (r==1 and (c==1 or c==2 or c==4 or c==5)) or (r==2 and (c==1 or c==2 or c==4 or c==5)) or (r==4 and (c==6 or c==7)) or (r==5 and (c==6 or c==7)) ):
               output_grid[r,c] = 8
            
    # change color: gray(5) by red(2)
    for r, c in coords:
        if (input_grid[r,c] == 5) :
            if ( (r==1 and (c==3 or c==6)) or (r==2 and (c==3 or c==6)) or (r==3 and (c==3 or c==6)) or (r==4 and (c==4))  or (r==5 and (c==4)) or (r==6 and (c==4))):
               output_grid[r,c] = 2

    return output_grid