# 67385a82 • 024 • refine_coder

---
```python
"""
The transformation involves changing the color of green pixels to azure if they are immediately to the left of any azure pixel.
"""

import numpy as np

def find_objects_by_color(grid, color):
    """
    Finds contiguous objects of a specific color in the grid.
    Returns a list of lists, where each inner list contains the (row, col) coordinates of pixels belonging to an object.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def get_right_adjacent_pixel(grid, r, c):
    """Returns the pixel to the right of (r, c), or None if it's out of bounds."""
    rows, cols = grid.shape
    if c + 1 < cols:
        return (r, c + 1)
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find green objects
    green_objects = find_objects_by_color(output_grid, 3)
    
    # find azure objects
    azure_objects = find_objects_by_color(input_grid, 8)

    # iterate through green objects
    for green_object in green_objects:
        for green_pixel in green_object:
            # check for right adjacency to any azure pixel
            right_adj = get_right_adjacent_pixel(input_grid, green_pixel[0], green_pixel[1])
            if right_adj:
                adj_r, adj_c = right_adj
                # check if the adjacent pixel is part of any azure object
                for azure_object in azure_objects:
                    if (adj_r, adj_c) in azure_object:
                        # change the green pixel to azure
                        output_grid[green_pixel[0], green_pixel[1]] = 8
                        break  # move to the next green pixel after a change

    return output_grid
```
