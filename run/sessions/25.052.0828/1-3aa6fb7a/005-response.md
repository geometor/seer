# 1-3aa6fb7a • 005 • example_2 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in this second example.

**YAML Block Observation:**

```yaml
observations:
  input_grid:
    - "7x7 grid with most cells being 0 (white)."
    - "Three separate objects of color 8 (azure):"
      - "Object 1: A horizontal line of two cells at position (0,4) and (0,5)."
      - "Object 2: A vertical line of two cells at position (2,2) and (3,2)."
      - "Object 3: A reversed L-shape consisting of three azure cells, at position (5,4), (6,3) and (6,4)."

  output_grid:
    - "7x7 grid, mostly identical to the input grid."
    - "Changes observed:"
      -   "The azure object at (0,4) and (0,5) has a blue pixel to the left of its right-most pixel."
      - "The azure object  at (2,2) and (3,2) has a blue pixel to the right of its top-most pixel"
      - "The azure object at (5,4), (6,3) and (6,4) has a blue pixel to the left of its right-most pixel"
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all objects of color 8 (azure) in the input grid.
2.  **Conditional Placement:**
    *   Check the surrounding cells to determine the relative position and shape of the objects:
        *   Identify each object as a vertical or horizontal line.

        *   If there is an object that is a vertical line:
            *   Place a cell with color 1 (blue) immediately to the right of the top most point of the object.

        *   If there is an object that is a horizontal line:

            *   Place a cell with color 1 (blue) immediately to the left of the right most point of the object.
        *   If an object is an "L" shape.
            *   Place a cell with color 1 (blue) immeditately to the left of the right most point of the object.
3.  **Preserve:** All other cells remain unchanged.

The core concept remains almost the same.

```python
"""
This program transforms the input grid as follows:
1. It identifies all objects of color 8 (azure) in the input grid.
2. It determines the shape of these objects (vertical or horizontal line).
3. Based on the shape and position:
    - For a vertical line, a cell with color 1 (blue) is placed to the right of the object's top.
    - For a horizontal line, a cell with color 1 (blue) is placed to the left of the object's rightmost point.
    - For an L shape, the same rule applies.
4. All other cells remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return []

        visited.add((x, y))
        object_coords = [(x, y)]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            object_coords.extend(dfs(x + dx, y + dy))

        return object_coords

    for x in range(grid.shape[0]):
      for y in range(grid.shape[1]):
        if grid[x,y] == color:
          found_object = dfs(x, y)
          if len(found_object) > 0:
            objects.append(found_object)

    return objects
    

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort the object coordinates to determine top-left and bottom-right
        sorted_obj = sorted(obj, key=lambda p: (p[0], p[1]))
        
        if len(obj) == 2:  # Check if it is a line
            # Determine if it is a vertical line or a horizontal line
            if sorted_obj[0][0] == sorted_obj[1][0]:  # Vertical Line
                top_point = sorted_obj[0]
                output_grid[top_point[0], top_point[1] + 1] = 1  # Place blue to the right of the top
            elif sorted_obj[0][1] == sorted_obj[1][1]:  # Horizontal
                right_point = sorted_obj[1] # extract rightmost point
                output_grid[right_point[0], right_point[1] - 1] = 1 # place to left
        elif len(obj) > 2: # the L shape
            #find the rightmost pixel
            right_most = sorted(obj, key=lambda p: p[1], reverse=True)[0]
            output_grid[right_most[0], right_most[1] - 1] = 1
    return output_grid
```

