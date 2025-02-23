# d5d6de2d • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify Red Shapes:** Locate all contiguous regions (objects) of red (value 2) pixels in the input grid.
2.  **Find inner pixels:** In the red area, locate the pixels such that all the 4 neighbors of it (top, down, left, right) are also red.
3.  **Draw Green shapes**: create new green shapes on the output grid where the pixels should be based on the output from step 2.
4. **Background**: rest of the pixels on output grid is white.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of the given color in the grid.

    Args:
        grid: The input grid.
        color: The color of the objects to find.

    Returns:
        A list of objects, where each object is a set of (row, col) coordinates.
    """    
    objects = []
    visited = set()
    rows, cols = len(grid), len(grid[0])

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r][c] != color:
            return
        visited.add((r, c))
        current_object.add((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and (r, c) not in visited:
                current_object = set()
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def get_inner_pixels(obj, grid):
    """
    Finds the inner pixels of an object.
    """
    inner_pixels = set()
    rows, cols = len(grid), len(grid[0])
    for r,c in obj:
      neighbors = [(r-1,c), (r+1, c), (r, c-1), (r, c+1)]
      is_inner = True
      for nr, nc in neighbors:
        if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]):
          is_inner = False
          break
      if is_inner:
          inner_pixels.add((r,c))

    return inner_pixels


def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # find red objects
    red_objects = get_objects(input_grid, 2)

    # find inner most red pixels
    for obj in red_objects:
      inner_pixels = get_inner_pixels(obj, input_grid)
      # create green shapes at inner positions
      for r, c in inner_pixels:
          output_grid[r][c] = 3
    

    return output_grid
```
