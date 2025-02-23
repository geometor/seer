"""
1.  **Identify Objects:** Find all contiguous regions of blue (1) pixels.
2.  **Preserve White:** Keep all white (0) pixels unchanged.
3.  **Inner Rectangle Rule**: Find blue objects completely enclosed within another, larger blue object. If it's at the top-left *within that enclosure*, change it to red (2). Note that "top-left" is relative to the enclosing object, not the entire grid.
4. **3x1 or 1x3 Rule**: Change a portion of a blue object that forms a 3x1 or 1x3 shape into orange (7).
5. **Other Blue Objects**: Blue objects or parts of blue objects that do not fit the above rule, do not change.
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
    

def get_top_left_object(objects, grid):
  """Finds the top-left object within an enclosure if available, otherwise return None"""
  enclosed_objects = []
  for obj in objects:
      for other_obj in objects:
        if is_enclosed(obj, other_obj, grid):
          enclosed_objects.append(obj)
          break

  if not enclosed_objects:
      return None
          
  enclosed_objects.sort(key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj)))
  return enclosed_objects[0]

def is_line(obj, grid):
    """ check if an object containts a 3x1 or 1x3 shape (horizontal or vertical)
        Returns the coordinates of the object that meets that condition
    """
    rows = [p[0] for p in obj]
    cols = [p[1] for p in obj]

    #check width and height of bounding box
    height = max(rows) - min(rows) + 1
    width = max(cols) - min(cols) + 1

    # Check for 3x1 vertical line
    if height >= 3 and width == 1:
      return obj
    
    # Check for 1x3 horizontal line
    if width >= 3 and height == 1:
      return obj

    if height >= 3 and width >= 1:
      # find all 3x1 lines
      lines = []
      for row in range(min(rows), max(rows) -1):
          for col in range(min(cols), max(cols)):
              if (row, col) in obj and (row + 1, col) in obj and (row + 2, col) in obj:
                  lines.append([(row, col), (row + 1, col), (row + 2, col)])
      if len(lines) > 0: return lines
    if width >= 3 and height >= 1:
        # find all 1x3 lines
        lines = []
        for col in range(min(cols), max(cols) - 1):
            for row in range(min(rows), max(rows)):
                if (row, col) in obj and (row, col + 1) in obj and (row, col + 2) in obj:
                    lines.append([(row, col), (row, col+1), (row, col+2)])
        if len(lines) > 0: return lines
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # find blue objects
    blue_objects = find_objects(input_grid, 1)
    
    # find top-left object
    top_left_obj = get_top_left_object(blue_objects, input_grid)
    if top_left_obj is not None:
      for row, col in top_left_obj:
        output_grid[row,col] = 2

    # find 3x1 or 1x3 objects
    for obj in blue_objects:
      line_coords = is_line(obj, input_grid)
      if line_coords is not None:
          if isinstance(line_coords[0], list): # is a list of lines
            for line in line_coords:
                for row, col in line:
                  output_grid[row, col] = 7
          else: #is just a line
              for row, col in line_coords:
                output_grid[row, col] = 7

    return output_grid