# 1-3aa6fb7a • 003 • example_2 - NLP

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC79F15E10>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC79F16EC0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
input_grid:
  objects:
    - color: 8
      shape: 'L-shape'
      position: (1,1) and connected cells
    - color: 8
      shape: 'L-shape'
      position: (3,4) and connected cells
  grid_size: (7,7)

output_grid:
    - color: 8
      shape: 'L-shape'
      position: (1,1) and connected cells
    - color: 8
      shape: 'L-shape'
      position: (3,4) and connected cells
    - color: 1
      shape: 'single cell'
      position: (2,1)
    - color: 1
      shape: 'single cell'
      position: (3,4)
  grid_size: (7,7)
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we can identify two distinct L-shaped objects, both composed of azure (color 8) cells. One located in top-left, the other in bottom-right.

2.  **Detect Change**: The L-shapes formed by color 8 are kept, and where each shape began, a color 1 is placed.

3. **Transformation Rule:** The program scans the input, keeps every shape, and adds a blue pixel (color 1) in the starting top-left cell of each color 8 shape.


```python
"""
The program scans the input, keeps every shape, and adds a blue pixel (color 1) in the starting top-left cell of each color 8 shape.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds and returns a list of objects of a specified color.
    Each object is a list of (row, col) tuples.
    """
    visited = set()
    objects = []

    def dfs(row, col, current_object):
        """
        Depth-First Search to find connected cells of the same color.
        """
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or (row, col) in visited
            or grid[row, col] != color
        ):
            return
        visited.add((row, col))
        current_object.append((row, col))
        # Explore adjacent cells
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_top_left(obj):
    """
    Return the top-left coordinate of the object
    """
    return min(obj,key=lambda x: (x[0],x[1]))
def transform(input_grid):
    """
    Transforms the input grid to generate an output grid based on L shapes.
    """
    # initialize output_grid as copy of input
    output_grid = np.copy(input_grid)

    # find objects
    objects_8 = find_objects(input_grid, 8)
    
    # change output pixels according to color 8 objects top-left corner
    for obj in objects_8:
      top_left = get_top_left(obj)
      output_grid[top_left[0],top_left[1]] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC79F166B0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC79F15C90>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
