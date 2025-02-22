"""
1. Identify Azure Lines: Find all objects in the input grid that are composed of the color azure (8).  Consider only objects that form a straight line, either horizontally or vertically.

2. Determine Line Orientation and Key Point: For each azure line:
    *   If the line is vertical, identify the topmost cell of the line.
    *   If the line is horizontal, identify the rightmost cell of the line.

3. Place Blue Cell:
    *   Vertical Line: Place a blue cell (color 1) immediately to the right of the topmost cell, if a right position exists.
    *   Horizontal Line: Place a blue cell (color 1) immediately to the left of the rightmost cell, if a left position exists.

4. Preserve Unchanged Cells: All other cells should remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return []

        visited.add((x, y))
        object_coords = [(x, y)]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            object_coords.extend(dfs(x + dx, y + dy))

        return object_coords

    for x in range(grid.shape[0]):
      for y in range(grid.shape[1]):
        if grid[x,y] == color:
          found_object = dfs(x, y)
          if len(found_object) > 0:
            objects.append(found_object)

    return objects
    

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort the object coordinates to determine top-left and bottom-right
        sorted_obj = sorted(obj, key=lambda p: (p[0], p[1]))

        if len(obj) == 2:  # Check if it is a line
            # Determine if it is a vertical line or a horizontal line
            if sorted_obj[0][0] == sorted_obj[1][0]:  # Vertical Line
                top_point = sorted_obj[0]
                # Check boundaries before placing blue cell
                if top_point[1] + 1 < output_grid.shape[1]:
                    output_grid[top_point[0], top_point[1] + 1] = 1  # Place blue to the right of the top
            elif sorted_obj[0][1] == sorted_obj[1][1]:  # Horizontal
                right_point = sorted_obj[1] # extract rightmost point
                # Check boundaries before placing blue cell
                if right_point[1] - 1 >= 0:
                    output_grid[right_point[0], right_point[1] - 1] = 1 # place to left
    return output_grid