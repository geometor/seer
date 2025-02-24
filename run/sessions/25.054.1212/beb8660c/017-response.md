# beb8660c • 017 • refine_coder

---
```python
"""
1.  **Identify Objects:** Find all contiguous blocks of non-black (non-zero) pixels. Consider each block as a single object.
2.  **Determine Stacking Order:** The objects in the input grid will be stacked at the bottom of the output grid. The order is determined by the original vertical positions of the objects, preserving their relative order from top to bottom in the input.
3. **Stack Objects:** Place each input object into the output grid, starting at the lowest available row. Maintain the original shape of each object. If an object occupies multiple rows, it should occupy the *lowest* rows it can.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    #very simplistic object detection - contiguous same color
    def get_objects(grid):
        visited = set()
        objects = []
        def dfs(r, c, color, obj):
            if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r,c] != color:
                return
            visited.add((r,c))
            obj.append((r,c))
            dfs(r+1, c, color, obj)
            dfs(r-1, c, color, obj)
            dfs(r, c+1, color, obj)
            dfs(r, c-1, color, obj)

        for r in range(grid.shape[0]):
            for c in range(grid.shape[1]):
                if (r,c) not in visited and grid[r,c]!=0:
                    obj = []
                    dfs(r, c, grid[r,c], obj)
                    objects.append(obj)
        return objects

    # Get objects and sort them by their top-most row (original vertical position)
    input_objects = get_objects(input_grid)
    input_objects.sort(key=lambda obj: min(r for r, c in obj))

    # change output pixels - stack objects
    for obj in input_objects:
        # Calculate the height of the object
        min_row = min(r for r, _ in obj)
        max_row = max(r for r, _ in obj)
        obj_height = max_row - min_row + 1

        # Find the lowest available row for this object
        start_row = output_grid.shape[0] - obj_height
        while start_row >= 0:
          #check if space if free - go up one row if not, else break
          collision = False
          for r_offset in range(obj_height):
            for r,c in obj:
                if r - min_row + start_row < output_grid.shape[0] and output_grid[r - min_row + start_row, c] != 0:
                  collision = True
                  break
            if collision:
              break
          if collision:
            start_row-=1
          else:
            break

        if start_row<0:
           continue #skip this object, no room

        # Place the object in the output grid
        for r, c in obj:
            output_grid[r - min_row + start_row, c] = input_grid[r, c]

    return output_grid
```
