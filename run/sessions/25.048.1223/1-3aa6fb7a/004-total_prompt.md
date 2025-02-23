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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7DEBC9512E90>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7DEBC95126E0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      positions:
        - (1, 1)
        - (2, 1)
        - (2, 2)
        - (3, 4)
        - (3, 5)
        - (4, 5)
      shape: Two separate L-shapes (or could be considered individual pixels)

output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      positions:
        - (1, 1)
        - (2, 1)
        - (2, 2)
        - (3, 4)
        - (3, 5)
        - (4, 5)
      shape:  Two separate L-shapes (same as input)
    - color: 1 (blue)
      positions:
        - (1,2)
        - (4,4)
      shape: single pixels
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all azure (color 8) colored pixels in the input grid. Note their positions.

2.  **Preserve:** Copy every azure pixel to the output grid, keeping its position unchanged.

3. **Detect Particular Shape:** The azure pixels form two separated 'L' shapes made of three pixels each.

4.  **Insert:** For each one of the two shapes, insert a blue (color 1) pixel inside the corner of the "L" shape. The blue pixel should connect the two lines of the "L".

**Step-by-step explanation of the transformation:**
The azure pixels did not move. The only change from the input to the output is the addition of blue pixels in the "elbows" of the two L-shapes.


*text:*
```python
"""
The transformation rule is as follows:
1. Copy all azure (color 8) pixels from the input grid to the output grid without changing their positions.
2. For each 3-pixel 'L' shape formed by the azure pixels, insert a blue (color 1) pixel in the corner of the "L".
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of the specified color."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def detect_l_shape(object_coords):
    """Detects if a set of coordinates forms an L shape."""
    if len(object_coords) != 3:
        return None

    # Convert to numpy array for easier calculations
    coords = np.array(object_coords)
    
    # Calculate distances between all pairs of points
    dist_matrix = np.sum((coords[:, np.newaxis, :] - coords[np.newaxis, :, :]) ** 2, axis=2)
    
    # Check for two distances of 1 and one distance of 2 (squared distances)
    distances = sorted(dist_matrix[np.triu_indices(3, 1)])

    if distances == [1, 1, 2]:       
        # Find the corner point (the point with distances 1 to both other points)
        for i in range(3):
            if dist_matrix[i, (i+1)%3] == 1 and dist_matrix[i, (i+2)%3] == 1:
                
                corner_index=i
                #find elbow
                other_indices = [(j % 3) for j in range(i + 1, i + 3)]

                elbow_row = object_coords[other_indices[0]][0] + object_coords[other_indices[1]][0] - object_coords[corner_index][0]
                elbow_col = object_coords[other_indices[0]][1] + object_coords[other_indices[1]][1] - object_coords[corner_index][1]



                return (elbow_row, elbow_col)

    return None


def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through objects and check for L-shapes
    for obj in azure_objects:
        l_corner = detect_l_shape(obj)
        if l_corner:
            output_grid[l_corner] = 1

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7DEBC95135E0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7DEBC95125C0>

*text:*
Okay, let's analyze the second example.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      positions:
        - (0, 4)
        - (0, 5)
        - (1, 5)
        - (2, 2)
        - (3, 2)
        - (3, 3)
        - (5, 4)
        - (6, 4)
        - (6, 3)

      shape: Three separate L-shapes.

output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      positions:
        - (0, 4)
        - (0, 5)
        - (1, 5)
        - (2, 2)
        - (3, 2)
        - (3, 3)
        - (5, 4)
        - (6, 4)
        - (6, 3)
      shape:  Three separate L-shapes (same as input).
    - color: 1 (blue)
      positions:
        - (1,4)
        - (2,3)
        - (5,3)
      shape: single pixels
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all azure (color 8) colored pixels in the input grid.
2.  **Preserve:** Copy all azure pixels to the output grid, keeping their position unchanged.
3.  **Detect L-Shapes:** Identify 3-pixel "L" shapes among the azure pixels. In this case, there are three such L-shapes.
4. **Insert Blue Pixel:** Place a blue (color 1) pixel inside the corner of each detected "L" shape.

**Step-by-step explanation:**

The transformation copies the azure pixels without modification.  The change involves adding a blue pixel to the "elbow" or inner corner of each 3-pixel L-shaped azure object. The code I wrote before correctly describes this general rule and it will work in this case.

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
