# 0e206a2e • 008 • example_2 • investigate_coder

---
```python
"""
Transforms the input grid by moving and arranging colored objects to the lower-right corner of the output grid. The order of arrangement is yellow, blue, green, and red. The green object serves as a base, starting at row 10.
"""

import numpy as np

def find_objects(grid):
    """
    Finds and returns a dictionary of colored objects in the grid.
    Each object is a list of (row, col) coordinates.
    """
    objects = {}
    visited = set()

    def dfs(row, col, color, obj):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)


    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            color = grid[row, col]
            if color != 0 and (row, col) not in visited:
                obj = []
                dfs(row, col, color, obj)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj)

    return objects

def transform(input_grid):
    # Initialize output grid with zeros (white)
    output_grid = np.zeros_like(input_grid)

    # Find objects in the input grid
    objects = find_objects(input_grid)
    
    # Define the order of colors for arrangement
    color_order = [4, 1, 3, 2]  # Yellow, Blue, Green, Red

    # Place the green object (color 3) starting at row 10
    if 3 in objects:
      green_objects = objects[3]
      #choose the large green object
      lengths = [len(obj) for obj in green_objects]
      max_length_index = lengths.index(max(lengths))
      green_obj = green_objects[max_length_index]

      # find bounding box.
      min_row = min(r for r, c in green_obj)
      #min_col = min(c for r, c in green_obj)
      
      #place object
      for r, c in green_obj:
          dr = r - min_row
          output_grid[10 + dr, 9 + (c-9)] = 3 # c - 9 for green starting point.

    # Place other colored objects
    current_row = 11
    current_col = 9
    for color in color_order:
        if color in objects:
          if color != 3:
            for obj in objects[color]:  # Handle multiple objects of the same color
                  min_row = min(r for r, c in obj)
                  min_col = min(c for r, c in obj)
                  for r, c in obj:
                      dr = r - min_row
                      dc = c - min_col
                      if(current_col + dc < input_grid.shape[1]):
                        output_grid[current_row+dr, current_col + dc] = color
            if color != 3:
              current_col += 1

    return output_grid
```
