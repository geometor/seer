# 67385a82 • 020 • example_4 • investigate_coder

---
```python
"""
The transformation involves changing some of the azure object to be consistent.
Specifically, changing the green-adjacent azure pixel on the right side of the first row of green pixel to azure color.
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

def get_adjacent_pixels(grid, r, c):
    """returns the adjacent pixels of a specified color"""
    rows, cols = grid.shape
    adjacent = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            adjacent.append((nr,nc))
    return adjacent
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find green objects
    green_objects = find_objects_by_color(output_grid, 3)
    
    # check the condition
    if green_objects:
        first_green_row = green_objects[0][0][0]
        for green_pixel in green_objects[0]:
            if green_pixel[0] == first_green_row:
               adj_pixels = get_adjacent_pixels(input_grid, green_pixel[0], green_pixel[1])
               for adj_r, adj_c in adj_pixels:
                   if input_grid[adj_r, adj_c] == 8:
                       output_grid[adj_r,adj_c] = 8
    
    #find objects
    azure_objects = find_objects_by_color(input_grid,8)

    # apply rule and change colors
    if green_objects:      
      for green_pixel in green_objects[0]:
        
        if green_pixel[0] == first_green_row : #first row condition
          adj_pixels = get_adjacent_pixels(input_grid, green_pixel[0], green_pixel[1])
          for adj_r, adj_c in adj_pixels:
            if input_grid[adj_r, adj_c] == 8:
                output_grid[1,1] = 8
    
    return output_grid
```
