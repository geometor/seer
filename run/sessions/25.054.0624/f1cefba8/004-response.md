# f1cefba8 • 004 • refine_coder

---
```python
"""
Preserve azure (8) pixels and selectively modify other color regions based on an alternating pattern and border detection.
"""

import numpy as np

def get_objects(grid):
    """
    Find contiguous regions of the same color, excluding white (0).
    Returns a dictionary of objects keyed by color.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, color, obj_coords):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
            return
        visited.add((r, c))
        obj_coords.append((r, c))
        dfs(r + 1, c, color, obj_coords)
        dfs(r - 1, c, color, obj_coords)
        dfs(r, c + 1, color, obj_coords)
        dfs(r, c - 1, color, obj_coords)
        dfs(r + 1, c+1, color, obj_coords)
        dfs(r + 1, c-1, color, obj_coords)
        dfs(r - 1, c+1, color, obj_coords)
        dfs(r - 1, c-1, color, obj_coords)


    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and (r, c) not in visited:
                obj_coords = []
                dfs(r, c, color, obj_coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_coords)
    return objects

def get_borders(grid, objects):
    """
    Identifies border pixels for each object.
    """
    rows, cols = grid.shape
    borders = {}

    for color, obj_list in objects.items():
        for obj_coords in obj_list:
            obj_borders = []
            for r, c in obj_coords:
                is_border = False
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr, nc] != color:
                                is_border = True
                                break  # optimization
                    if is_border:
                        break  # optimization
                if is_border:
                    obj_borders.append((r,c))
            if color not in borders:
                borders[color] = []

            borders[color].extend(obj_borders)

    return borders

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Objects
    objects = get_objects(input_grid)

    # 2. Find Borders
    borders = get_borders(input_grid, objects)
    # print(borders)

    # 3. Preserve Azure (8)
    #  - Already handled by copying the input grid

    # 4. Alternate and Transform
    for color, obj_list in objects.items():
        if color != 8: # Not azure
              for obj in obj_list:
                for r, c in obj:
                    output_grid[r,c] = 0
              border_color = None

              for obj in obj_list:
                min_r = min(r for r, c in obj)
                max_r = max(r for r, c in obj)
                min_c = min(c for r, c in obj)
                max_c = max(c for r, c in obj)

                for r, c in obj:
                    if border_color is None:
                        for dr in [-1,0,1]:
                            for dc in [-1,0,1]:
                                if (dr != 0 or dc !=0):
                                    new_r = r + dr
                                    new_c = c + dc
                                    if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols:
                                        if (new_r, new_c) not in obj:
                                          neighbor_color = input_grid[new_r, new_c]
                                          if neighbor_color != 0 and neighbor_color != 8:
                                            border_color = neighbor_color

                    if (r-min_r) % 2 == 0 and (c - min_c) %2 == 0:
                        output_grid[r,c] = color if border_color is None else border_color
                    elif (r-min_r) % 2 == 1 and (c - min_c) %2 == 1:
                        output_grid[r,c] = color if border_color is None else border_color
                    elif (r-min_r) % 2 == 1 and (c - min_c) %2 == 0:
                        if color in [2,3]:
                          output_grid[r,c] = 0

                    elif (r-min_r) % 2 == 0 and (c - min_c) %2 == 1:
                        if color in [2,3]:
                          output_grid[r,c] = 0


    for color, border_coords in borders.items():
      if color != 8:
          for r,c in border_coords:
              output_grid[r,c] = 0

    return output_grid
```
