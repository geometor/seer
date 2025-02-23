# 1-3aa6fb7a • 008 • example_2 - CODE

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

Here's a YAML block summarizing my initial observations:


```yaml
observations:
  - grid_size: 7x7
  - colors:
    - present: [0, 8]
    - added: [1]
  - object_shapes:
      - "two separate L shaped objects of color 8"
  - relative_positions:
    - object_1: top-left
    - object_2: bottom-right, mirrored orientation of object_1
```


Here's my step-by-step description of the transformation:

1.  **Identify Objects:** The input grid contains two distinct "L"-shaped objects made of azure (color 8) pixels.

2.  **Object 1 Transformation**: The top-left "L" shape remains unchanged.

3.  **Object 2 Transformation**: In the bottom right "L" shaped object color: a single pixel in the corner of the "L", specifically the second to the rightmost and second to the bottommost azure, is changed to blue (value 1).

In essence, the transformation involves changing single corner azure pixel of the mirrored L object in the bottom-right of the input grid to the color blue.

```python
"""
The transformation identifies two "L"-shaped azure objects in the input grid. The top-left "L" shape remains unchanged. 
The bottom-right "L" shape has its corner pixel changed to blue (value 1).
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of (corner_row, corner_col) tuples for each L-shape.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L shape (2x2 block with one missing corner)
                neighbors = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                color_count = sum(1 for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color)
                if color_count == 2:
                    l_shapes.append((r, c))
    return l_shapes

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the L-shaped objects of color azure (8)
    l_shapes = find_l_shapes(input_grid, 8)
    
    # Find corner for color change
    if len(l_shapes) > 1:
        # Identify corner of the L-shape
        
        # Find the bottom-right L-shape
        max_row = -1
        bottom_right_l = None
        for r,c in l_shapes:
          if r >= max_row:
            max_row = r
            bottom_right_l = (r,c)

        # find the coordinates of the inside corner and make it blue
        corner_row, corner_col = bottom_right_l
        output_grid[corner_row+1, corner_col+1] = 1

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

![Image](007-example_2_input.png)


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

![Image](007-example_2_output.png)

Okay, let's analyze the second example pair. Here's the YAML block with my observations:


```yaml
observations:
  - grid_size: 7x7
  - colors:
    - present: [0, 8]
    - added: [1]
  - object_shapes:
    - "three separate L shaped objects of color 8"
  - relative_positions:
    - object_1: top-right
    - object_2: middle-left
    - object_3: bottom-right, mirrored orientation of object_2
```


Here's my step-by-step description of the transformation:

1.  **Identify Objects:** The input grid contains three distinct "L"-shaped objects made of azure (color 8) pixels.

2.  **Object Transformations**: Locate the *inside corner* of each L-shape.
    *   If the L is in the top row, the inside corner is one down and one left from the corner
    *   If the L is in the left column, the inside corner is one right and one down from the corner
    *   If the L is in the bottom row (and not the left column), the inside corner is one up and one right.

3.  Change the color of the pixel at each inside corner to blue (1)

The rule is to change the inside corner of each azure L-shaped object to blue. The previous solution attempted to find *all* L-shapes but then only modified the bottom-right one. This new example and description modifies all L-shapes.

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
