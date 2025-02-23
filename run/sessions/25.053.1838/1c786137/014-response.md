# 1c786137 • 014 • example_3 - CODE

---
```python
"""
1.  **Identify Objects:** Treat contiguous blocks of the same color within the input grid as individual objects.
2.  **Filter Objects:** Remove the largest object, which takes more than 25% of the image (the large azure '8' region in this example).
3.  **Create a Bounding Box:** For the remaining pixels, find a bounding box.
4. **Output the Bounding box** Construct the output grid from the bounding box.
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

def transform(input_grid):
    # Identify Objects
    objects = find_objects(input_grid)

    # Filter Objects (remove largest object)
    total_pixels = input_grid.size
    largest_object = max(objects, key=len, default=[])
    if len(largest_object) / total_pixels > 0.25:
      objects.remove(largest_object)

    # Get all remaining points
    remaining_points = []
    for obj in objects:
      remaining_points.extend(obj)

    # Create Bounding Box
    min_r, min_c, max_r, max_c = bounding_box(remaining_points)


    # Initialize the output grid
    output_grid = np.zeros((max_r-min_r+1, max_c-min_c+1), dtype=int)

    # Fill output grid
    for r, c in remaining_points:
      output_grid[r-min_r, c-min_c] = input_grid[r,c]

    return output_grid
```
