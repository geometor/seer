"""
The gray object is transformed into azure and red objects. The azure color is assigned to the positions of gray where the left neighbor of that position is also gray and the position is not on the most left side of the shape. The red color is placed on the other positions.
"""

import numpy as np

def get_objects(grid):
    """
    Identify contiguous regions of the same color as objects.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, current_object):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, color, current_object)
        dfs(row - 1, col, color, current_object)
        dfs(row, col + 1, color, current_object)
        dfs(row, col - 1, color, current_object)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                color = grid[row, col]
                if color != 0:  # Ignore background color
                    current_object = []
                    dfs(row, col, color, current_object)
                    objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Get gray object
    gray_objects = get_objects(input_grid)
    
    # Assuming there is only one object which is gray colored
    if len(gray_objects) != 1:
        print("There is no gray object.")
    else:
      gray_object = gray_objects[0]

      # Separate object
      for (row, col) in gray_object:
          is_azure = False
          
          # Check the left neighbor
          if col > 0 and input_grid[row, col-1] == 5:
              is_azure = True
          
          if is_azure:
              output_grid[row, col] = 8
          else:
              output_grid[row, col] = 2

    return output_grid