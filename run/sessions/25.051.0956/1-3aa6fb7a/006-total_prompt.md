# 1-3aa6fb7a • 006 • example_2 - CODE

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

Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
observations:
  input_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape
        position: (1,1) # Top-left corner of the object
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (3,4) # Top-left corner of the object
  output_grid:
      - object_1:
          color: 8 (azure)
          shape: L-shape
          position: (1,1)
      - object_2:
          color: 8 (azure)
          shape: L-shape
          position: (3,4)
      - object_3:
          color: 1 (blue)
          shape: single cell
          position: (1,2)
      - object_4:
          color: 1(blue)
          shape: single cell
          position: (4,5)
```

**Natural Language Program:**

1.  **Identify Objects:** In the input grid, we can see two L-shaped objects made of azure (color 8) pixels.

2.  **Preserve Objects:** These objects keep shape, color and location in the output grid.

3. **Add blue pixel:** In the output, a blue pixel (color 1) appears on the right of the corner of each object.

**Transformation Rule (In Natural Language):**

The transformation preserves the two azure L-shaped objects, maintaining their original positions and shapes. Additionally, it adds a single blue pixel (color 1) to the right of each object's corner, in both cases.

```python
"""
The transformation preserves the two azure L-shaped objects, maintaining their original positions and shapes. Additionally, it adds a single blue pixel (color 1) to the right of each object's corner, in both cases.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_l_shape_corner(object_coords):
    # Find the bounding box
    min_r = min(r for r, c in object_coords)
    max_r = max(r for r, c in object_coords)
    min_c = min(c for r, c in object_coords)
    max_c = max(c for r, c in object_coords)

    # Check all four corners of the bounding box to determine which one is part of the object
    if (min_r, min_c) in object_coords:
      return min_r, min_c
    elif (min_r, max_c) in object_coords:
      return min_r, max_c
    elif (max_r, min_c) in object_coords:
       return max_r, min_c
    else:
      return max_r, max_c

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
      corner = find_l_shape_corner(obj)

      # check which corner is the L
      if (corner[0]+1,corner[1]) in obj and (corner[0], corner[1]+1) in obj: # topleft
        output_grid[corner[0], corner[1] + 2] = 1 # add blue at right
      elif (corner[0]-1,corner[1]) in obj and (corner[0], corner[1]+1) in obj: # bottomleft
        output_grid[corner[0] , corner[1] + 2] = 1 # add blue at right
      elif (corner[0]-1,corner[1]) in obj and (corner[0], corner[1]-1) in obj: # bottomnright
        output_grid[corner[0] , corner[1]] = 1 # add blue at right
      else: # topright
        output_grid[corner[0], corner[1] ] = 1


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

Okay, let's analyze the transformation between the input and output grids for the second example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape
        position: (0,4) # Top-left corner of the object
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (2,2) # Top-left corner of the object
    - object_3:
        color: 8 (azure)
        shape: L-shape
        position: (5,4)
    - object_4:
      color: 8 (azure)
      shape: L-shape
      position: (6,3)

  output_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape
        position: (0,4)
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (2,2)
    - object_3:
        color: 8 (azure)
        shape: L-shape
        position: (5,4)
    - object_4:
      color: 8 (azure)
      shape: L-shape
      position: (6,3)
    - object_5:
        color: 1 (blue)
        shape: single cell
        position: (1,5)
    - object_6:
        color: 1 (blue)
        shape: single cell
        position: (2,3)
    - object_7:
      color: 1 (blue)
      shape: single cell
      position: (5,3)
```

**Natural Language Program:**

1.  **Identify Objects:** In the input grid, there are four L-shaped objects made of azure (color 8) pixels.

2.  **Preserve Objects:** These objects maintain their shape, color, and location in the output grid.

3.  **Add Blue Pixel:**  A blue pixel (color 1) is added to the right of the corner of each L-shaped object, similar to the first example.

**Transformation Rule (In Natural Language):**

The transformation preserves all four azure L-shaped objects, keeping their original positions and shapes.  A single blue pixel (color 1) is added to the right side of the corner pixel of each L-shaped object. The logic is consistent with the previous example, but applied to four objects instead of two.

**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
