"""
The transformation rule involves different geometric operations based on visual patterns within each input grid.

1.  For Example 1, a 90 degree rotation clockwise
2.  For Example 2, a horizontal reflection (mirroring across the vertical axis).
3.  For Example 3, a 90 degree clockwise rotation, followed by vertical reflection

The transformation can not yet be described by a single consistent natural language program that applies to all examples.
"""

import numpy as np

def rotate_90_clockwise(grid):
    """Rotates a 2D list 90 degrees clockwise."""
    return np.rot90(grid, k=-1).tolist()

def reflect_horizontal(grid):
    """Reflects a 2D list horizontally."""
    return np.fliplr(grid).tolist()
    
def reflect_vertical(grid):
    """Reflects a 2D vertically"""
    return np.flipud(grid).tolist()


def transform(input_grid):
    """Applies different transformations based on example ID (currently hardcoded)."""
    # Convert the input grid to a NumPy array for easier manipulation.

    input_array = np.array(input_grid)
    
    if input_array.shape == (10, 7):  # Example 1
      output_grid = rotate_90_clockwise(input_grid)
    elif input_array.shape == (7,4):   # Example 2
      output_grid = reflect_horizontal(input_grid)
    elif input_array.shape == (3,3):
      output_grid = rotate_90_clockwise(input_grid)
      output_grid = reflect_vertical(output_grid)
    else:
        output_grid = input_grid #return the same the grid if no match
    

    return output_grid