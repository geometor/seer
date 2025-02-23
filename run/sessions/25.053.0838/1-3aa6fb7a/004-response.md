# 1-3aa6fb7a • 004 • refine_coder

---
```python
"""
1.  **Identify Azure Objects:** Find all contiguous groups of azure (8) pixels. Each group constitutes an "azure object."
2.  **Find Adjacent White Pixels:** For each azure object, identify all white (0) pixels directly adjacent (up, down, left, or right) to any pixel in the azure object.
3. **Determine Blue Pixel Placement:**
   *  For each azure object:
       * Locate the top-left most azure pixel. If there is a white pixel directly to the right of this pixel, color this white pixel blue (1).
       * Otherwise, locate the top-right most azure pixel. If there is a white pixel directly above it, color it blue.
       * If neither, do not add any new colored pixel.

4.  **Output:** The modified grid with the newly colored blue pixels is the output.
"""

import numpy as np

def get_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def get_adjacent_pixels(grid, object_pixels, adj_color):
    adjacent = []
    for r, c in object_pixels:
        neighbors = [
            (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)
        ]
        for nr, nc in neighbors:
            if (0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and
                    grid[nr, nc] == adj_color):
                adjacent.append((nr, nc))
    # remove duplicates
    adjacent = list(dict.fromkeys(adjacent))
    return adjacent

def get_top_left_pixel(object_pixels):
    return min(object_pixels)

def get_top_right_pixel(object_pixels):
     # Sort by column (descending) then row (ascending)
    return sorted(object_pixels, key=lambda x: (-x[1], x[0]))[0]


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    # Identify azure objects
    azure_objects = get_objects(input_grid, 8)
    # find adjacent white pixels and change the color
    for obj in azure_objects:
        top_left = get_top_left_pixel(obj)
        top_right = get_top_right_pixel(obj)

        right_of_top_left = (top_left[0], top_left[1] + 1)
        above_top_right = (top_right[0] - 1, top_right[1])

        if (0 <= right_of_top_left[0] < output_grid.shape[0] and
            0 <= right_of_top_left[1] < output_grid.shape[1] and
            output_grid[right_of_top_left] == 0):
            output_grid[right_of_top_left] = 1

        elif (0 <= above_top_right[0] < output_grid.shape[0] and
            0 <= above_top_right[1] < output_grid.shape[1] and
            output_grid[above_top_right] == 0):
             output_grid[above_top_right] = 1

    return output_grid
```
