# 0e206a2e • 004 • refine_coder

---
```python
"""
Transforms the input grid by moving connected regions of non-white pixels vertically. Objects in the upper half of the grid move down, and objects in the lower half move up. The movement continues until an object hits the grid boundary or another object, causing objects to stack.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all contiguous regions (objects) of non-white (non-zero) pixels in the grid.

    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    visited = set()
    objects = []

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] == 0:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] != 0 and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def calculate_centroid(object_coords):
    """
    Calculates the centroid (center of mass) of an object.
    """
    rows, cols = zip(*object_coords)
    return np.mean(rows), np.mean(cols)

def move_object(grid, object_coords, direction):
    """
    Moves an object's coordinates in the given direction, checking for collisions.

    `direction`: 1 for down, -1 for up.
    Returns: new object coordinates, and boolean indicating if move was possible
    """
    new_object_coords = []
    moved = True
    for row, col in object_coords:
        new_row = row + direction
        if not (0 <= new_row < grid.shape[0]):
          moved = False  # Hit grid boundary
          break;
        if grid[new_row, col] != 0 and (new_row, col) not in object_coords:
          moved = False # Hit another object.
          break;
        new_object_coords.append((new_row, col))
    
    if not moved:
      return object_coords, False # return original, not moved
    return new_object_coords, True # return new and moved == True

def transform(input_grid):
    # initialize output_grid
    grid = np.array(input_grid)  # work with numpy array
    output_grid = np.array(input_grid)  # Start with a copy of input

    # Find all objects
    objects = find_objects(grid)
    
    # sort objects by their vertical position (centroid row)
    objects.sort(key=lambda obj: calculate_centroid(obj)[0])

    # build the output grid progressively
    
    vertical_center = grid.shape[0] / 2
    
    moved_objects = []

    for obj in objects:
        color = grid[obj[0][0], obj[0][1]] # save the color
        centroid_row, _ = calculate_centroid(obj)
        direction = 1 if centroid_row < vertical_center else -1

        # clear object from grid, work with copy.
        temp_grid = np.copy(output_grid)
        for r,c in obj:
          temp_grid[r,c] = 0

        # Move object
        moved_object = obj
        moved = True
        while moved:
            moved_object, moved = move_object(temp_grid, moved_object, direction)

        # add moved object to output
        for row, col in moved_object:
            temp_grid[row, col] = color

        output_grid = temp_grid # update

    return output_grid.tolist() # return as list
```
