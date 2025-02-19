"""
The input azure L-shapes had their upper-right and lower-left corner pixels changed to blue.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_corners(object_coords):
    """
    Finds the upper-right and lower-left corner of an L-shaped object.
    It receives the object coordinates assuming the object is L-shaped.
    It returns None values if can't define the corners.
    """
    if not object_coords:
      return None, None
    
    # Find min and max row, and min and max col
    min_row = min(r for r, c in object_coords)
    max_row = max(r for r, c in object_coords)
    min_col = min(c for r, c in object_coords)
    max_col = max(c for r, c in object_coords)
    
    # Create a set for faster lookup
    coords_set = set(object_coords)
    
    # Infer corners based on the L shape
    upper_right = None
    lower_left = None

    if (min_row, max_col) in coords_set:
      upper_right = (min_row, max_col)
    if (max_row, min_col) in coords_set:
      lower_left = (max_row, min_col)    

    return upper_right, lower_left

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    The input azure L-shapes had their upper-right and lower-left corner pixels changed to blue.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)
    
    corners = []

    # Find and store the corners of each object in a list
    for obj in azure_objects:
        upper_right, lower_left = find_corners(obj)
        if upper_right:
          corners.append(upper_right)
        if lower_left:
          corners.append(lower_left)
    
    # Change the identified corner pixels to color 1 (blue)
    for corner in corners:
      output_grid[corner] = 1    

    return output_grid