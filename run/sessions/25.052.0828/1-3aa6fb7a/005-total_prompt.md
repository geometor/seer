# 1-3aa6fb7a • 005 • example_2 - NLP

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block Observation:**

```yaml
observations:
  input_grid:
    - "7x7 grid with most cells being 0 (white)."
    - "Two separate objects of color 8 (azure):"
      - "Object 1: A vertical line of two cells at position (1,1) and (2,1)."
      - "Object 2: A horizontal line of two cells at position (3,4) and (4,4)."
  output_grid:
    - "7x7 grid, mostly identical to the input grid."
    - "Changes observed:"
      - "The azure object at (1,1) has color 1 (blue) put to its right at (2,1)"
      - "The azure object at (4,4) has color 1(blue) put to its left at (4,3) "
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all objects of color 8 (azure) in the input grid.
2.  **Conditional Placement:**
    *   Check the surrounding cells to determine the relative position and shape of the objects:

    *   If there is an object that is an vertical line:
        *    Place a cell with color 1 (blue) immediately to the right of the top most point of the object.

    *    If there is an object that is a horizontal line:
        *   Place a cell with color 1 (blue) immediately to the left of the right most point of the object.
3.  **Preserve:** All other cells remain unchanged.

```python
"""
This program transforms the input grid as follows:
1. It identifies all objects of color 8 (azure) in the input grid.
2. It determines the shape of these objects (vertical or horizontal line).
3. Based on the shape and position:
    - For a vertical line, a cell with color 1 (blue) is placed to the right of the object's top.
    - For a horizontal line, a cell with color 1 (blue) is placed to the left of the object's rightmost point.
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
    return output_grid
```

**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

![Image](005-example_2_input.png)


**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

![Image](005-example_2_output.png)

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
