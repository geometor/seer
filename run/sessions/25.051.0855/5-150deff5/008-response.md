# 5-150deff5 • 008 • refine_code - CODE

---
```python
import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of (row, col) tuples representing the object's pixels.
    """
    objects = []
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return []

        visited.add((row, col))
        region = [(row, col)]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            region.extend(dfs(row + dr, col + dc))
        
        return region

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c))

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule.
    """
    output_grid = np.copy(input_grid)
    gray_objects = find_objects(input_grid, 5)

    # Find min and max columns of all gray pixels
    all_gray_pixels = [pixel for obj in gray_objects for pixel in obj]

    if not all_gray_pixels:
        return output_grid

    min_col_all = min(c for r, c in all_gray_pixels)
    max_col_all = max(c for r, c in all_gray_pixels)
    avg_col_all = (min_col_all + max_col_all) / 2


    for obj in gray_objects:
        min_col = min(c for r, c in obj)
        max_col = max(c for r, c in obj)
        
        if min_col <= avg_col_all or max_col >= avg_col_all:
          for r, c in obj:
              output_grid[r,c] = 8
        else:
          for r,c in obj:
            output_grid[r,c] = 2
    
    return output_grid
```

