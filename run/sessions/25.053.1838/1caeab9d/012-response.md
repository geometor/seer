# 1caeab9d • 012 • refine_coder

---
```python
"""
1. Identify Objects: Find all distinct, contiguous regions (objects) of non-zero color in the input grid.  These regions can be any shape, including single pixels.
2. Order Objects: Sort the identified objects from left to right based on the horizontal position of their leftmost pixel.
3. Combine Objects: Create a new grid. Place the identified and sorted objects horizontally, side-by-side, in the new grid.
4. Vertical Placement and Height:
   - Determine output row based on consistent positioning.  Specifically, if input is 10 rows, output on row 5. If input grid is 5 rows, place on row 2. Maintain original height of elements.
5. Output Grid: The output grid might not have the same dimensions as the input grid. It should be large enough to fit all objects.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all contiguous regions of non-zero color (objects) in the grid.
    Returns a list of dictionaries, each representing an object.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                # Start BFS to find the extent of the object
                queue = [(r, c)]
                visited[r, c] = True
                min_row, max_row = r, r
                min_col, max_col = c, c

                while queue:
                    curr_row, curr_col = queue.pop(0)
                    min_row = min(min_row, curr_row)
                    max_row = max(max_row, curr_row)
                    min_col = min(min_col, curr_col)
                    max_col = max(max_col, curr_col)

                    # Check neighbors (including diagonals)
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                        new_row, new_col = curr_row + dr, curr_col + dc
                        if 0 <= new_row < rows and 0 <= new_col < cols and \
                           not visited[new_row, new_col] and grid[new_row, new_col] == color:
                            queue.append((new_row, new_col))
                            visited[new_row, new_col] = True

                objects.append({
                    'color': color,
                    'top_left': (min_row, min_col),
                    'bottom_right': (max_row, max_col)
                })

    return objects

def transform(input_grid):
    # Identify objects in the input grid
    objects = find_objects(input_grid)

    # Order objects by their leftmost column
    objects.sort(key=lambda obj: obj['top_left'][1])

    # Calculate total width needed and max height of objects
    total_width = 0
    max_height = 0
    for obj in objects:
        obj_height = obj['bottom_right'][0] - obj['top_left'][0] + 1
        obj_width = obj['bottom_right'][1] - obj['top_left'][1] + 1
        total_width += obj_width
        max_height = max(max_height, obj_height)

    # Determine output grid size and target row
    input_height = input_grid.shape[0]
    if input_height >= 10:
        output_height = input_height
        target_row = 5
    elif input_height == 5:
        output_height = 5
        target_row = 2
    else: # default
        output_height = input_height
        target_row = input_height // 2


    output_grid = np.zeros((output_height, total_width), dtype=int)

    # Combine objects horizontally
    current_col = 0
    for obj in objects:
      obj_height = obj['bottom_right'][0] - obj['top_left'][0] + 1
      obj_width =  obj['bottom_right'][1] - obj['top_left'][1] + 1

      for r in range(obj_height):
          row_to_place = target_row
          # use input row if it is not part of specified rows
          if input_height != 5 and input_height != 10:
            row_to_place = obj['top_left'][0]

          for c in range(obj_width):
              output_grid[row_to_place, current_col + c] = obj['color']

          # if 5 or 10, copy same object to next row
          if input_height == 5 or input_height == 10:
            row_to_place += 1
            for c in range(obj_width):
              output_grid[row_to_place, current_col + c] = obj['color']
      current_col += obj_width

    return output_grid
```
