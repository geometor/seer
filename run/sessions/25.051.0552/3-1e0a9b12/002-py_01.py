"""
The transformation rule is as follows:
Every object in the input grid moves down a number of rows equal to its original row number. 
The background (color 0) remains unchanged. The two yellow objects merge.
"""

import numpy as np

def find_objects(grid):
    """
    Finds and returns a list of objects in the grid.
    Each object is a dictionary with color and positions.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                color = grid[r, c]
                positions = [(r, c)]
                objects.append({'color': color, 'positions': positions})
                visited.add((r, c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Each object moves down a number of rows equal to its original row number.
    """
    # Initialize output grid with the same dimensions and background color
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Find objects in the input grid
    objects = find_objects(input_grid)
    
    # Move each object down by its original row number
    for obj in objects:
        color = obj['color']
        for pos in obj['positions']:
          row, col = pos
          new_row = row + row  # Move down by the original row number
          if new_row < output_grid.shape[0]:
              if color == 4:
                 output_grid[new_row,col]=4
              else:
                output_grid[new_row, col] = color
          else:
             if color == 4:
                 output_grid[row,col]=4
             else:
                output_grid[row, col] = color # if row goes beyond boundary, object disappears

    
    return output_grid