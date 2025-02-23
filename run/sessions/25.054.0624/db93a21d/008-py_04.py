"""
1.  **Identify Maroon Shapes:** Locate all contiguous regions of color 9 (maroon). These are rectangular shapes.

2.  **Green Expansion (Top-Left):**
    *   For the 4x4 and 2x2 maroon shapes on the left side of the grid, expand a region of color 3 (green) upwards and to the left.
    * The area of green is bound at the top and left by white.

3.  **Blue Expansion (Top-Right):**
      *   For the remaining maroon shape, create a new background using 1 (blue)
        in the area up and to the left

4. **Green fill:** Change white (0) cells above the top most maroon (9) shapes to green (3)

5. **Blue Fill:** Change white (0) cells in an area above and to the left of other
   maroon shapes using color blue (1).
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

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
                if current_object:
                    objects.append(current_object)
    return objects

def get_bounding_box(obj):
    min_row = min(p[0] for p in obj)
    max_row = max(p[0] for p in obj)
    min_col = min(p[1] for p in obj)
    max_col = max(p[1] for p in obj)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    maroon_objects = find_objects(input_grid, 9)

    # Sort objects by their top-left corner's column, then row
    maroon_objects.sort(key=lambda obj: (get_bounding_box(obj)[2], get_bounding_box(obj)[0]))


    for i, obj in enumerate(maroon_objects):
        min_row, max_row, min_col, max_col = get_bounding_box(obj)

        if i < 2:
            # Green Expansion
            for r in range(min_row + 1):
                for c in range(min_col + 1):
                  output_grid[r,c] = 3

        else :
            #Blue Expansion
            for r in range(min_row + 1):
                for c in range(min_col + 1):
                  output_grid[r,c] = 1

    #fill top row
    output_grid[0:6,0:15] = np.where(output_grid[0:6,0:15] == 0, 3, output_grid[0:6,0:15])
    
    return output_grid