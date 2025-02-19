# 1f642eb9 • 003 • example_2 - NLP

---
Okay, let's analyze the second transformation.

**YAML Description of Observations**

```yaml
input_grid:
  size: 10x10
  objects:
    - color: 7
      shape: single cell
      position: (0, 4)
    - color: 8
      shape: 3x4 rectangle
      position: (3, 3)
    - color: 6
      shape: single cell
      position: (3, 0)
    - color: 2
      shape: single cell
      position: (5, 9)
    - color: 3
      shape: single cell
      position: (7, 0)
    - color: 1
      shape: single cell
      position: (9, 5)

output_grid:
  size: 10x10
  objects:
    - color: 7
      shape: single cell
      position: (3, 4)
    - color: 8
      shape: 3x3 rectangle, and a 1x1
      position: (3,3) and (3,5)
    - color: 6
      shape: single cell, and a 1x1
      position: (3, 0) and (3,3)
    - color: 2
      shape: single cell, and a 1x1
      position: (5, 9) and (5,5)
    - color: 3
      shape: single cell, and a 1x1
      position: (7, 0) and (7,3)
     - color: 1
      shape: single cell, and a 1x1
      position: (9, 5) and (7,5)
```

**Natural Language Program: Transformation Rule**

1.  **Identify Objects:**  We have four single-color cells (7, 6, 2, 3 and 1) and one larger rectangular object of color 8.

2. **Move the single cells:**
    - Color 7 stays in the same position of the input and adds a new cell in the input, on top of the 8 object.
    - Colors 6, 3, and 1 each combine with the closest object made of color 8, creating new objects made of two cells, each new object made of colors 8 and 6, 3 and 1, respectively.
    - The 8 object loses one of its cells, the one on column 5 and row 3.

3. **Move 8:**
    - The cell at the position (3,5) on the object with color 8 is removed and it is placed to the right side of number 2, at the same row.

4.  **Summary**: Number 7 adds a cell to the top of the main object. The rest of the numbers combines with 8 on the left side of it. Number 2 combines with the cell that was removed.

```python
"""
Number 7 adds a cell to the top of the main object. The rest of the numbers combines with 8 on the left side of it. Number 2 combines with the cell that was removed.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color."""
    objects = {}
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, obj_coords):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]
                or visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        obj_coords.append((row, col))
        dfs(row + 1, col, color, obj_coords)
        dfs(row - 1, col, color, obj_coords)
        dfs(row, col + 1, color, obj_coords)
        dfs(row, col - 1, color, obj_coords)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row,col] != 0:
                color = grid[row, col]
                obj_coords = []
                dfs(row, col, color, obj_coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_coords)

    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()

    # Find objects in the input grid
    objects = find_objects(input_grid)

    # Find the '8' object (assuming there's only one)
    eight_object = objects.get(8)[0]  # List of coordinates of the '8' object
    
    # Get top left corner of the eight_object
    eight_object_rows = [coord[0] for coord in eight_object]
    eight_object_cols = [coord[1] for coord in eight_object]
    
    eight_top_row = min(eight_object_rows)
    eight_left_col = min(eight_object_cols)
    eight_bottom_row = max(eight_object_rows)

    # Move '7'
    output_grid[eight_top_row, eight_left_col ] = 7

    # Move '6'
    six_coords = objects.get(6)[0][0]
    output_grid[eight_top_row, eight_left_col-1] = 6
    
    #Move 3
    three_coords = objects.get(3)[0][0]
    output_grid[eight_bottom_row, eight_left_col -1] = 3

    # Move '2'
    two_coords = objects.get(2)[0][0]
    output_grid[two_coords[0], eight_left_col + 2] = 2    

    #Move 1
    one_coords = objects.get(1)[0][0]
    output_grid[eight_bottom_row, eight_left_col+1] = 1    
    
    # Move '8'
    output_grid[eight_top_row, eight_left_col+2] = 0

    return output_grid
```

