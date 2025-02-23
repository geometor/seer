"""
The transformation identifies and removes "noisy" objects based on size and
replaces them with a padding of the most common background color.
The objects are then filled back based on rules that apply to object size, shape, and color
"""

import numpy as np
from collections import Counter

def get_objects(grid):
    """Identifies connected components (objects) in the grid."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] == 0:
            return
        visited.add((row, col))
        current_object.append(((row, col), grid[row, col]))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] != 0 and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects


def get_background_color(grid):
    """
    Determines the most common background color in the grid.
    Assumes background is color 0.
    """
    # Flatten grid and convert to list of pixel values
    pixels = grid.flatten().tolist()
    
    return 0

def transform(input_grid):
    """Transforms the input grid by removing and reconstructing objects."""
    
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid) # initialize to all zeros
    background_color = get_background_color(input_grid)

    # Get objects from the original grid
    original_objects = get_objects(input_grid)

    # Fill large and medium-sized structured objects back into the output grid
    for obj in original_objects:
        coords, color = zip(*obj)
        coords_array = np.array(coords)
        rows_obj = coords_array[:, 0]
        cols_obj = coords_array[:, 1]
        min_row, max_row = np.min(rows_obj), np.max(rows_obj)
        min_col, max_col = np.min(cols_obj), np.max(cols_obj)
            
        width = max_col - min_col + 1
        height = max_row - min_row + 1
        size = len(obj)

        if size >= 9: # large objects
            if height > 2 and width > 2:
                for (r, c), val in obj:
                  output_grid[r,c] = val
            
        elif size >=3 and size <=8: # medium-sized objects
              if height > 1 and width > 1: # structured object
                    for (r, c), val in obj:
                      output_grid[r,c] = val
              
        else: # small objects - remove noise
             pass
                      
    return output_grid