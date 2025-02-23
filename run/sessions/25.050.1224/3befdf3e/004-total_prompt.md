# 3befdf3e • 004 • example_2 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 0
0 0 0 4 6 4 0 0 0 0
0 0 0 4 4 4 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABAB7AAD0>

**output**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 0 0 0 0
0 0 4 6 6 6 4 0 0 0
0 0 4 6 4 6 4 0 0 0
0 0 4 6 6 6 4 0 0 0
0 0 0 4 4 4 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABAB79CF0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 4 # Yellow
      shape: rectangle
      position: (3,3) # Top-left corner of the rectangle
      size: (3,3) # 3x3 rectangle
      properties:
        - Contains a single magenta (6) cell in the center.
    - color: 6 # Magenta
      shape: single cell
      position: (4,4)
      size: (1,1)

output_grid:
  objects:
    - color: 4 # Yellow
      shape: rectangle
      position: (2,2) # Top-left corner
      size: (5,5)
      properties:
        - Contains a 3x3 magenta square in the center
    - color: 6
      shape: rectangle
      position: (3,3)
      size: (3,3)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the core object:** In the input grid, there is a 3x3 yellow (color 4) rectangle with a magenta (color 6) cell at its center.

2.  **Describe Object Expansion and Predicates:**
    -   The yellow rectangle *expands* by one cell in all directions (up, down, left, and right.)
    -   The central magenta cell *expands* to become a 3x3 rectangle.
    -   The expansion occurs vertically and horizontally.

3.  **Describe Action:**
   -   The existing yellow shape grows by one layer, keeping its square form.
   -    The central magenta dot grows by one cell up and down, and to the sides, to make a 3x3 square.

**Transformation Rule Summary**

The transformation rule is an expansion of both the outer yellow rectangle and the inner magenta cell. The yellow rectangle expands outwards by one cell in all directions, and the magenta cell expands to a 3x3 rectangle.

```python
"""
The transformation rule is an expansion of both the outer yellow rectangle and the inner magenta cell. The yellow rectangle expands outwards by one cell in all directions, and the magenta cell expands to a 3x3 rectangle.
"""

import numpy as np

def get_objects(grid):
    """Finds distinct objects in the grid based on color contiguity."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                object_coords = []
                queue = [(r, c)]
                visited[r, c] = True

                while queue:
                    curr_r, curr_c = queue.pop(0)
                    object_coords.append((curr_r, curr_c))

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_r, new_c = curr_r + dr, curr_c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r, new_c] and grid[new_r, new_c] == color:
                            queue.append((new_r, new_c))
                            visited[new_r, new_c] = True

                objects.append((color, object_coords))
    return objects
def transform(input_grid):
    """Transforms the input grid according to the expansion rule."""

    # Initialize output grid with zeros
    output_grid = np.zeros_like(input_grid)

    # Get objects from the input grid
    objects = get_objects(input_grid)

    yellow_object = None
    magenta_object = None

    for color, coords in objects:
        if color == 4:
            yellow_object = coords
        elif color == 6:
            magenta_object = coords

    # Expand yellow object
    if yellow_object:
        min_r = min(r for r, c in yellow_object)
        max_r = max(r for r, c in yellow_object)
        min_c = min(c for r, c in yellow_object)
        max_c = max(c for r, c in yellow_object)

        for r in range(min_r - 1, max_r + 2):
            for c in range(min_c - 1, max_c + 2):
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 4

    # Expand magenta object
    if magenta_object:
        center_r = magenta_object[0][0]  # Assuming it's a single cell
        center_c = magenta_object[0][1]

        for r in range(center_r - 1, center_r + 2):
            for c in range(center_c - 1, center_c + 2):
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 6

    return output_grid
```

**input**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 2 2 2 2 0 0 0
0 0 0 2 7 7 2 0 0 0
0 0 0 2 7 7 2 0 0 0
0 0 0 2 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABAB06A70>

**output**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 2 2 2 2 0 0 0
0 0 0 2 2 2 2 0 0 0
0 2 2 7 7 7 7 2 2 0
0 2 2 7 2 2 7 2 2 0
0 2 2 7 2 2 7 2 2 0
0 2 2 7 7 7 7 2 2 0
0 0 0 2 2 2 2 0 0 0
0 0 0 2 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABAB7A800>
Okay, let's analyze the second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 2 # Red
      shape: rectangle
      position: (3,3)
      size: (4,4)
      properties:
        - Contains a 2x2 orange (7) square in the center.
    - color: 7 # Orange
      shape: rectangle
      position: (4,4)
      size: (2,2)

output_grid:
  objects:
    - color: 2 # Red
      shape:  "cross-like" or plus sign + surrounding cells
      position: (1,3) #relative
      size: (7,4) #approximate, the filled area
      properties:
        - Contains a larger, more complex orange shape, formed around the initial orange object
    - color: 7 # Orange
      shape: "cross-like" or plus sign
      position: (3,3)
      size: (3,4)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the core objects:**
    *   A 4x4 red (color 2) rectangle.
    *   A 2x2 orange (color 7) square inside the red rectangle.

2.  **Describe Object Interactions, Predicates, and Actions:**
    *   The 2x2 orange square expands. It expands to a cross-like shape, composed of orange at the center and four "arms" extending north, south, east and west. The vertical "arm" is of length three.
    *   The red shape expands vertically and horizontally. The top and bottom rows of the red shape are copied up/down by one row. And an additional two cells on each side appear to make the final shape.

3.  **Transformation as Action:**
    -   The orange 2x2 shape transforms into a cross, keeping its center, and expanding up, down and sideways.
    -    The red cells 'move' to accommodate and surround the new shape of the orange object.
**Transformation Rule Summary**

The transformation involves two main actions: The inner orange square expands into a cross-like shape, and the outer red rectangle expands and reshapes to fit and to surround the expanded orange object.

```python
"""
The transformation involves two main actions: The inner orange square expands into a cross-like shape, and the outer red rectangle expands and reshapes to fit and to surround the expanded orange object.
"""
import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the orange object
    orange_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 7:
                orange_coords.append((r, c))

    # Expand the orange object into cross shape
    if orange_coords:
      min_or = min(r for r,c in orange_coords)
      max_or = max(r for r,c in orange_coords)
      min_oc = min(c for r,c in orange_coords)
      max_oc = max(c for r,c in orange_coords)

      center_r = (min_or + max_or) //2
      center_c = (min_oc + max_oc) //2

      #central square
      for r in range(rows):
        for c in range(cols):
          if input_grid[r,c] == 7:
            output_grid[r,c] = 7
      #vertical arm
      output_grid[center_r -1, center_c] = 7
      output_grid[center_r -1, center_c + 1] = 7

    # find red object
    red_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r,c] == 2:
              red_coords.append((r,c))
    if red_coords:
      min_rr = min(r for r, c in red_coords)
      max_rr = max(r for r, c in red_coords)
      min_rc = min(c for r, c in red_coords)
      max_rc = max(c for r, c in red_coords)
      # copy first and last rows
      for c in range(min_rc, max_rc+1):
        if min_rr > 0:
            output_grid[min_rr-1, c] = 2
        if max_rr < rows -1:
            output_grid[max_rr+1,c] = 2
      # add columns
      for r in range(min_rr-1, max_rr + 2):

          if min_oc > 0:
              output_grid[r,min_oc-1] = 2
          if max_oc < cols-1:
              output_grid[r,max_oc+2] = 2

          if 0 <= r < rows:
              if min_rc>0:
                  output_grid[r,min_rc-1] = 2
              if max_rc < cols -1:
                  output_grid[r,max_rc+1] = 2

    return output_grid
```

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
