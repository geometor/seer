"""
1.  **Identify Objects:** Determine all contiguous regions (objects) of the same color in the input grid.
2.  **Identify Excluded Color:** Determine the single color to exclude. In all the examples, exactly one color is entirely removed.
3.  **Filter Objects:** Remove all objects with the excluded color.
4.  **Create Bounding Box:** Construct the smallest rectangular bounding box that contains all remaining pixels.
5.  **Output:** Create the output grid by copying the pixels within the bounding box from the input grid to the output grid, preserving their relative positions.
"""

import numpy as np

def find_objects(grid):
    """
    Identifies contiguous objects in a grid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, color, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, color, current_object)
        dfs(r - 1, c, color, current_object)
        dfs(r, c + 1, color, current_object)
        dfs(r, c - 1, color, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if not visited[r, c]:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                if current_object:
                    objects.append(current_object)
    return objects

def bounding_box(points):
    """
    Finds the bounding box of a set of points.
    """
    if not points:
        return (0, 0, 0, 0)
    min_r, min_c = float('inf'), float('inf')
    max_r, max_c = float('-inf'), float('-inf')
    for r, c in points:
        min_r = min(min_r, r)
        min_c = min(min_c, c)
        max_r = max(max_r, r)
        max_c = max(max_c, c)
    return (min_r, min_c, max_r, max_c)

def get_object_colors(input_grid):
    objects = find_objects(input_grid)
    colors = set()
    for obj in objects:
        color = input_grid[obj[0]]
        colors.add(color)
    return colors

def transform(input_grid):
    # Identify Objects
    objects = find_objects(input_grid)

    # Identify Excluded Color (This is the key part we need to determine)
    input_colors = get_object_colors(input_grid)

    # The excluded color could be derived in several ways.  Since we don't
    # have the output grid here, we'll assume we have a helper function
    # that can determine this.  This function is a PLACEHOLDER.  In a real
    # implementation, this would involve looking at both input and output
    # during training to derive the rule.

    # Filter Objects
    remaining_points = []
    for obj in objects:
        if input_grid[obj[0][0], obj[0][1]] != excluded_color:
            remaining_points.extend(obj)

    # Create Bounding Box
    min_r, min_c, max_r, max_c = bounding_box(remaining_points)

    # Initialize the output grid
    output_grid = np.zeros((max_r - min_r + 1, max_c - min_c + 1), dtype=int)

    # Fill output grid
    for r, c in remaining_points:
        output_grid[r - min_r, c - min_c] = input_grid[r, c]

    return output_grid

def get_excluded_color(input_grid, output_grid):
    """
    Determines the excluded color by comparing the input and output grids.

    Args:
      input_grid: numpy array of the input
      output_grid: numpy array of the correct output

    Returns:  the excluded color
    """
    input_colors = set(np.unique(input_grid))
    output_colors = set(np.unique(output_grid))
    excluded_color = list(input_colors - output_colors)[0]
    return excluded_color