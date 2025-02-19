"""
Transformation Rule:

1. Identify azure (color 8) pixels in the input grid.
2. Check if the identified azure pixel has only azure neighbors to its left.
3. If so, change the pixel to the right of the azure pixel to blue (color 1) in the output grid.
4. Copy all other pixels from the input grid to the output grid.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Returns a dictionary of the neighbor coordinates and colors around a given cell.
    """
    rows, cols = grid.shape
    neighbors = {}

    # Define relative positions of neighbors
    positions = {
        'left': (0, -1),
        'right': (0, 1),
        'up': (-1, 0),
        'down': (1, 0)
    }
    
    for pos_name, (row_offset, col_offset) in positions.items():
        neighbor_row, neighbor_col = row + row_offset, col + col_offset
        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
            neighbors[pos_name] = (neighbor_row, neighbor_col, grid[neighbor_row, neighbor_col])
        else:
            neighbors[pos_name] = None
    
    return neighbors

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Change to blue the pixel to the right of each isolated azure pixel.
    An isolated azure pixel is any azure pixel having only azure neighbors to its left.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 8:  # Check for azure pixels
                neighbors = get_neighbors(input_grid, row, col)
                
                is_isolated = True
                #check if on the left there are only azure pixels
                if neighbors['left'] is not None:
                  if neighbors['left'][2] != 8:
                    is_isolated = False

                # if the pixel to the right is not azure and it is isolated, color it to blue
                if neighbors['right'] is not None and is_isolated:
                  output_grid[neighbors['right'][0], neighbors['right'][1]] = 1

    return output_grid