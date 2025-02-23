"""
The transformation identifies the two azure L-shaped objects and adds a single blue pixel adjacent to a specific point on each of those objects. The first object is identified on the top-left side, and the second L-shaped object is identified on the middle-right side. The rest of the azure pixels remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of the specified color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        """Depth-first search to find contiguous cells."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_l_shape(object_coords):
    """Checks if a set of coordinates forms an L-shape (normal or inverted)."""
    if len(object_coords) != 3:
        return False

    # Convert list of tuples to a NumPy array for easier manipulation
    coords = np.array(object_coords)

    # Calculate differences between consecutive x and y coordinates
    dx = np.diff(coords[:, 0])
    dy = np.diff(coords[:, 1])
    
    if (np.all(dx == 0) and np.all(np.abs(dy) == 1)) or \
            (np.all(dy == 0) and np.all(np.abs(dx) == 1)):
      return False
    
    # Check for L-shape (2x1, 1x2)
    x_values = coords[:,0]
    y_values = coords[:,1]

    x_range = max(x_values) - min(x_values)
    y_range = max(y_values) - min(y_values)

    return (x_range == 1 and y_range ==1)

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Filter for L-shaped objects
    l_shaped_objects = [obj for obj in azure_objects if is_l_shape(obj)]
    l_shaped_objects.sort(key=lambda obj: (obj[0][0], obj[0][1]))  #sort by top-left

    if len(l_shaped_objects) >= 1:
      first_l_shape = l_shaped_objects[0]
      first_l_shape.sort()
      topmost_pixel = first_l_shape[0]  #top-left
      output_grid[topmost_pixel[0], topmost_pixel[1] + 1] = 1  #put blue to the right

    if len(l_shaped_objects) >= 2:
      second_l_shape = l_shaped_objects[1]
      second_l_shape.sort(reverse=True) # sort by down-right
      bottommost_pixel = second_l_shape[0]  # bottom-right
      output_grid[bottommost_pixel[0], bottommost_pixel[1] - 1] = 1   #put blue to the left

    return output_grid