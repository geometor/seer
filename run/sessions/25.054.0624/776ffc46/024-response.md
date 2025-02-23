# 776ffc46 • 024 • refine_coder

---
```python
"""
1.  **Object Identification:** Identify all contiguous regions (objects) of the same color in the input grid.

2.  **Target Identification**:
    *   Look for objects that exist as "islands" inside other colors - that is, an object that is completely contained by another, larger object.
    *   There may be multiple "island" objects, but only one target object will transform.
    *   The "island" object can have other colors inside it.

3.  **Transformation:**
    *   Find the "island" objects
    *   Change the target object to red (color 2).

4.  **Output:** The output grid is identical to the input, except for the transformed target object.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all contiguous regions of the same color.
    Returns a dictionary where keys are colors and values are lists of object coordinates.
    """
    visited = set()
    objects = {}

    def dfs(r, c, color, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, color, current_object)
        dfs(r - 1, c, color, current_object)
        dfs(r, c + 1, color, current_object)
        dfs(r, c - 1, color, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            color = grid[r, c]
            if (r, c) not in visited:
                current_object = []
                dfs(r, c, color, current_object)
                if color not in objects:
                    objects[color] = []
                objects[color].append(current_object)
    return objects

def is_enclosed(object_coords, enclosing_color, grid):
    """
    Checks if an object is enclosed by a given color.
    """
    rows, cols = grid.shape
    for r, c in object_coords:
        # Check neighbors (up, down, left, right)
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr, nc] != enclosing_color and (nr, nc) not in object_coords:
                  return False
            elif (nr,nc) not in object_coords:
                # if we have hit a boundary and its not part of the object, it is not enclosed
                return False
    return True

def find_target_object(objects, grid):
    """
    Identifies enclosed objects, prioritizing blue then, finds the target object.
    """
    
    potential_targets = []
    
    for color, obj_list in objects.items():
        for obj_coords in obj_list:
            enclosing_colors = set()
            rows, cols = grid.shape
            for r, c in obj_coords:
              # Check neighbors (up, down, left, right)
              neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
              for nr, nc in neighbors:
                  if 0 <= nr < rows and 0 <= nc < cols:
                      if grid[nr, nc] != color:
                          enclosing_colors.add(grid[nr,nc])
            # Check that is it full surrounded
            if len(enclosing_colors) == 1:
                enclosing_color = enclosing_colors.pop()
                if is_enclosed(obj_coords, enclosing_color, grid):
                  potential_targets.append((color,obj_coords))

    # find the blue object, if available, otherwise, return the first potential object
    target_object = None
    for color, obj in potential_targets:
        if color == 1: # look for blue
          target_object = obj
          break

    if not target_object and len(potential_targets) > 0:
        target_object = potential_targets[0][1] # first object

    return target_object

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find all objects
    objects = find_objects(input_grid)

    # Locate the target object
    target_object = find_target_object(objects, input_grid)

    # Change the target object's color to red (2)
    if target_object:
        for r, c in target_object:
            output_grid[r, c] = 2

    return output_grid
```
