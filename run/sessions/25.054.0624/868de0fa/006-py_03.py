"""
1.  **Identify Objects:** Find all contiguous regions of blue (1) pixels. These are considered blue objects.
2.  **Preserve White:** White (0) pixels remain unchanged.
3.  **Inner Rectangle Rule:** Identify blue objects that are fully enclosed *within* another, larger blue object. The top-leftmost pixel of an enclosed object becomes red (2).
4. **Outer Rectangle Rule:** For all blue objects, examine the outer edge. If the blue object contains any 3x1 or 1x3 section of adjacent blue pixels, change *only those pixels* to orange.
5.  **Remaining**: All other blue pixels remain blue.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous regions (objects) of a specific color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        """Depth-First Search to explore contiguous regions."""
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
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_enclosed(obj, other_obj, grid):
    """Checks if obj is completely enclosed within other_obj."""
    if obj == other_obj:
        return False

    obj_rows, obj_cols = zip(*obj)
    min_obj_row, max_obj_row = min(obj_rows), max(obj_rows)
    min_obj_col, max_obj_col = min(obj_cols), max(obj_cols)

    other_obj_rows, other_obj_cols = zip(*other_obj)
    min_other_row, max_other_row = min(other_obj_rows), max(other_obj_rows)
    min_other_col, max_other_col = min(other_obj_cols), max(other_obj_cols)
    
    # Check if obj is within the bounds of other_obj
    if (min_obj_row > min_other_row and max_obj_row < max_other_row and
        min_obj_col > min_other_col and max_obj_col < max_other_col):
        return True
    return False
    

def get_top_left_pixel(obj):
    """Returns the top-left pixel of an object."""
    obj.sort(key=lambda p: (p[0], p[1]))
    return obj[0]

def find_lines(obj):
    """Finds 3x1 and 1x3 lines within an object."""
    lines = []
    rows, cols = zip(*obj)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    # Check for 3x1 lines
    for r in range(min_row, max_row - 1):
        for c in range(min_col, max_col + 1):
            if (r, c) in obj and (r + 1, c) in obj and (r + 2, c) in obj:
                lines.append([(r, c), (r + 1, c), (r + 2, c)])

    # Check for 1x3 lines
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col - 1):
            if (r, c) in obj and (r, c + 1) in obj and (r, c + 2) in obj:
                lines.append([(r, c), (r, c + 1), (r, c + 2)])

    return lines

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # find blue objects
    blue_objects = find_objects(input_grid, 1)
    
    # Apply Inner Rectangle Rule
    for obj in blue_objects:
        for other_obj in blue_objects:
            if is_enclosed(obj, other_obj, input_grid):
                top_left_pixel = get_top_left_pixel(obj)
                output_grid[top_left_pixel] = 2
                break  # Only one top-left per enclosure

    # Apply Outer Rectangle Rule
    for obj in blue_objects:
      lines = find_lines(obj)
      for line in lines:
          for row, col in line:
              output_grid[row, col] = 7

    return output_grid