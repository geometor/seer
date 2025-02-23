# 1-3aa6fb7a • 004 • example_2 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x712F67D0A260>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x712F67D0ABC0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: Two separate azure 'L' shapes.
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: Two separate azure 'L' shapes.
    - color: 1
      positions: [(1,2), (4,4)]
      shape: single blue pixels.
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can identify two distinct L-shaped objects made of azure (color 8) pixels.

2.  **Detect Change:** The azure objects are the same in the input and the output. The change are two blue pixels.

3. **Pinpoint blue change:**
     - Add a blue pixel to the right of the top left azure pixel.
     - Add a blue pixel to the left of the bottom right azure pixel.

**Transformation Rule Summary**

The azure L-shaped objects are unchanged. Blue pixels (color 1) are added, if possible, horizontally adjacent (left/right) to azure pixels belonging to an L-shaped structure, where such addition does not change the overall L shape of the object.

```python
"""
The azure L-shaped objects are unchanged. Blue pixels (color 1) are added, if possible, horizontally adjacent (left/right) to azure pixels belonging to an L-shaped structure, where such addition does not change the overall L shape of the object.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous regions of the same color in the grid.
    Returns a dictionary where keys are colors and values are lists of pixel coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, color, obj):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
            return
        visited.add((r, c))
        obj.append((r, c))
        dfs(r + 1, c, color, obj)
        dfs(r - 1, c, color, obj)
        dfs(r, c + 1, color, obj)
        dfs(r, c - 1, color, obj)

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                color = grid[r, c]
                obj = []
                dfs(r, c, color, obj)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj)
    return objects

def is_l_shape(obj, grid):
    """
    Checks if a given object (list of coordinates) forms an L-shape.
    """
    if len(obj) != 3:
        return False

    # Convert coordinates to numpy array for easier calculations
    coords = np.array(obj)
    
    # Calculate differences between coordinates
    diffs = np.diff(coords, axis=0)

    
    if not (np.all(diffs[:, 0] >= 0) or np.all(diffs[:, 0] <= 0)):
        return False
        
    if not (np.all(diffs[:, 1] >= 0) or np.all(diffs[:,1] <= 0)):
        return False
    
    # check that is an "L" and not a line
    
    d1 = [ obj[1][0] - obj[0][0] , obj[1][1] - obj[0][1] ]
    d2 = [ obj[2][0] - obj[1][0] , obj[2][1] - obj[1][1] ]

    if d1[0] != 0 and d1[1] != 0: return False
    if d2[0] != 0 and d2[1] != 0: return False

    return True
    

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    objects = get_objects(input_grid)

    if 8 in objects:
        for obj in objects[8]:
            if is_l_shape(obj, input_grid):
                #find topleft and bottomright
                obj_coords = np.array(obj)
                top_left_index = np.argmin(obj_coords.sum(axis=1))
                bottom_right_index = np.argmax(obj_coords.sum(axis=1))
                top_left = obj[top_left_index]
                bottom_right = obj[bottom_right_index]
                
                # Add blue pixel to the right of top_left, within bounds.
                if top_left[1] + 1 < cols:
                  output_grid[top_left[0], top_left[1] + 1] = 1
                # Add blue pixel to the left of bottom_right, within bounds
                if bottom_right[1] -1 >= 0:
                  output_grid[bottom_right[0] , bottom_right[1] - 1] = 1
                  

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x712F67D0AB90>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x712F67D0A620>
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5,4), (6,3),(6,4)]
      shape: Three separate azure 'L' shapes.
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5,4), (6,3),(6,4)]
      shape: Three separate azure 'L' shapes.
    - color: 1
      positions: [(1, 4), (2, 3), (5,3)]
      shape: single blue pixels.
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, there are three distinct L-shaped objects made of azure (color 8) pixels.

2.  **Detect Change:** The azure colored pixels are unchanged. The change occurs through the addition of three blue pixels.

3. **Pinpoint blue change:**

    *   For each azure "L" shaped object add a blue pixel immediately to the left or to the right of the corner pixel forming the L, if available. The selection criterion between available empty space to the left and right is not specified and we have to consider either option valid.

**Transformation Rule Summary**
The rule is consistent with the previous example.

The azure L-shaped objects are unchanged. Blue pixels (color 1) are added, if possible, horizontally adjacent (left/right) to the *corner* azure pixels belonging to an L-shaped structure.

The provided python program implements this rule and I don't see the need to change it.

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
