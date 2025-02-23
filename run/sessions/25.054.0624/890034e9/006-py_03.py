"""
1.  **Identify Target Objects:** Find all contiguous regions (objects) of a specific color in the input grid. The target color is the color that forms a closed shape.
2.  **Identify Interior Colors:** Within each target object's bounding box, check for a specific "interior" color. The interior colors are the colors enclosed by the target color shape.
3.  **Conditional Fill:**
    *   If a target object contains the specified "interior" colors:
        * Change any pixels matching a third color within the bounding box to that interior color. The third color is *not* the target color, nor the 'background' color in the interior, but another color contained inside.

4. All other objects remain the same.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous regions of the specified color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col):
        """Depth-first search to find connected components."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return []

        visited[row, col] = True
        region = [(row, col)]

        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))
        return region

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                objects.append(dfs(row, col))
    return objects

def get_bounding_box(region):
    """Calculates the bounding box of a region."""
    min_row = min(r for r, c in region)
    max_row = max(r for r, c in region)
    min_col = min(c for r, c in region)
    max_col = max(c for r, c in region)
    return min_row, max_row, min_col, max_col

def contains_color(grid, bbox, color):
    """Checks if a bounding box contains a specific color."""
    min_row, max_row, min_col, max_col = bbox
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if grid[row, col] == color:
                return True
    return False

def find_interior_color(grid, bbox, target_color):
    """Find the interior color within a bounding box, excluding the target and a background color."""
    min_row, max_row, min_col, max_col = bbox
    colors_inside = set()
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if grid[row,col] != target_color:
                colors_inside.add(grid[row, col])

    if len(colors_inside) > 1: #more than one color
      # find background color
      background_color = -1
      max_count = 0
      for color in colors_inside:
          count = 0
          for row in range(min_row, max_row + 1):
              for col in range(min_col, max_col + 1):
                if grid[row,col] == color:
                    count +=1
          if count > max_count:
                max_count = count
                background_color = color
      #return a non-background color
      for color in colors_inside:
        if color != background_color:
          return color

    return None  # No distinct interior color found

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Determine the target color and interior color based on the input.

    target_color = None
    interior_color = None

    # Iterate through all colors to find a potential target
    for color in np.unique(input_grid):
        objects = find_objects(input_grid, color)
        if len(objects) == 0:
            continue

        for obj in objects:
          bbox = get_bounding_box(obj)
          found_interior_color = find_interior_color(input_grid, bbox, color)

          if found_interior_color is not None: #if target object contains interior color
              target_color = color
              interior_color = found_interior_color
              break
        if target_color is not None:
          break

    if target_color is None:
      return output_grid


    # Find target objects
    target_objects = find_objects(input_grid, target_color)

    for target_object in target_objects:
        bbox = get_bounding_box(target_object)
        min_row, max_row, min_col, max_col = bbox

        #check if it contains interior color
        if interior_color is not None:
            for row in range(min_row, max_row+1):
                for col in range(min_col, max_col+1):
                  # Find third color within the bounding box that is not background or target color, to be filled
                    if grid[row, col] != target_color and grid[row,col] != 0 and contains_color(input_grid, bbox, grid[row,col]) : # there is some third color within
                        output_grid[row,col] = interior_color

    return output_grid