"""
1.  **Identify Green Objects:** Find all contiguous regions of green pixels.
2.  **Determine Leftmost Green Object:** Sort the green objects by their leftmost column coordinate. The object with the smallest leftmost column is the leftmost green object.
3.  **Leftmost Green Expansion Down:** The leftmost green object expands vertically downwards to the bottom edge of the grid. This expansion does not change the color of any other object.
4.  **Identify Rightmost Green Object:** Identify the rightmost green object by selecting the green object with the largest column value.   
5.  **Identify Adjacent Red Objects:** Find the red object adjacent to the right side of the rightmost green object.
6.  **Expand Red to the bottom:** The red pixels adjacent to the rightmost green object are extended downwards to the bottom of the grid.
"""

import numpy as np

def find_objects(grid, color):
    """Find contiguous regions of a specific color."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
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

def get_object_bounds(obj):
    """Get the bounding box of an object."""
    min_row = min(p[0] for p in obj)
    max_row = max(p[0] for p in obj)
    min_col = min(p[1] for p in obj)
    max_col = max(p[1] for p in obj)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    height, width = input_grid.shape

    # 1. Identify Green Objects
    green_objects = find_objects(input_grid, 3)

    # 2. Determine Leftmost Green Object and 3. Leftmost Green Expansion
    if green_objects:
        green_objects.sort(key=lambda obj: min(p[1] for p in obj))
        left_green_object = green_objects[0]
        min_row, max_row, min_col, max_col = get_object_bounds(left_green_object)

        for col in range(min_col, max_col + 1):
            for row in range(min_row, height):
                output_grid[row, col] = 3

    # 4. Identify Rightmost Green object and 5. Identify Red Objects
    if len(green_objects) > 1:
       green_objects.sort(key=lambda obj: max(p[1] for p in obj))
       right_green_object = green_objects[0] # select the *rightmost*
       _, _, _, max_col_r = get_object_bounds(right_green_object)
       red_objects = find_objects(input_grid, 2)
       
       # 6. Expand Red to bottom
       for red_object in red_objects:
            for r_row, r_col in red_object:
              if r_col == max_col_r:
                  for row in range(r_row, height):
                      output_grid[row,r_col] = 2

    return output_grid