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

**Observations and Documentation**

Here's a YAML block summarizing my initial observations:

```yaml
task: 001-example_1
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        instances:
          - shape: L-shape
            position: (1,1) # Top-left corner of the bounding box
            size: 2x2
          - shape: reverse L-shape
            position: (3,4) # Top-left corner of the bounding box
            size: 2x2
      - color: 0 (white)
        instances:
          - shape: background
            position: (0,0)
            size: 7x7
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        instances:
          - shape: L-shape
            position: (1,1)
            size: 2x2
          - shape: reverse L-shape
            position: (3,4)
            size: 2x2
      - color: 1 (blue)
        instances:
          - shape: single cell
            position: (1,2)
            size: 1x1
          - shape: single cell
            position: (4,5)
            size: 1x1
      - color: 0 (white)
        instances:
          - shape: background
            position: (0,0)
            size: 7x7
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Objects:** Two azure (color 8) L-shaped objects are present in the input grid. One is a regular "L" shape, and the other is a reversed "L".

2.  **Locate Change:** We need to find where within each L-shaped object a blue pixel is inserted. Examining positions (1,2) for first L-shaped object and (4,5) for the second one, we find that these match the right-most and bottom-most pixel location of the L-shaped objects.

3.  **Transformation Rule:**
    *   Preserve the two azure (color 8) L-shaped objects in their original positions.
    *   Change the color of the right-most pixel of first azure L-shape from azure (8) to blue (1).
    *   Change the color of the bottom-most pixel of second azure L-shape from azure (8) to blue (1).

**Natural Language Program**
Here is the program in natural language:
1. Copy the input to the output.
2. For the first L-shaped azure object in the top-left quadrant of the grid:
   - Find the right-most cell occupied by that object.
   - Change the color of that cell from 8 to 1.

3. For the second L-shaped azure object in the bottom-right quadrant:
   - Find the bottom-most cell occupied by that object.
   - Change the color of that cell from 8 to 1.

```python
"""
Copies the input grid to the output grid, then finds two specific L-shaped azure objects.
For the first L-shape, it changes the right-most pixel to blue.
For the second L-shape, it changes the bottom-most pixel to blue.
"""

import numpy as np

def find_l_shapes(grid, color):
    # helper function for finding objects
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if not is_valid(x, y) or visited[x, y] or grid[x, y] != color:
            return

        visited[x, y] = True
        current_object.append((x, y))

        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and not visited[x, y]:
                current_object = []
                dfs(x, y, current_object)
                # check for approximate shape and size (could be enhanced with other geometric checks)
                if 3 <= len(current_object) <= 5:
                    objects.append(current_object)

    return objects

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    # assume that two L-shaped will be in this order
    if len(l_shapes) >= 2:

        # process first L-shape (top-left)
        first_l_shape = l_shapes[0]
        # find right-most pixel
        rightmost_pixel = max(first_l_shape, key=lambda p: p[1])
        output_grid[rightmost_pixel] = 1


        # process second L-shape (bottom-right)
        second_l_shape = l_shapes[1]
        # Find the bottom-most pixel
        bottommost_pixel = max(second_l_shape, key=lambda p: p[0])  # bottom-most
        output_grid[bottommost_pixel] = 1

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

**Observations and Documentation**

```yaml
task: 005-example_2
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        instances:
          - shape: reverse L-shape
            position: (0,4) # Top-left corner of the bounding box
            size: 2x3
          - shape: L-shape
            position: (2,2)
            size: 2x2
          - shape: reverse L-shape
             position: (5,3)
             size: 2x2

      - color: 0 (white)
        instances:
          - shape: background
            position: (0,0)
            size: 7x7
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        instances:
          - shape: reverse L-shape
            position: (0,4)
            size: 2x3
          - shape: L-shape
            position: (2,2)
            size: 2x2
          - shape: reverse L-shape
            position: (5,3)
            size: 2x2
      - color: 1 (blue)
        instances:
          - shape: single cell
            position: (1,4)
            size: 1x1
          - shape: single cell
            position: (2,3)
            size: 1x1
          - shape: single cell
            position: (5,3)
            size: 1x1
      - color: 0 (white)
        instances:
          - shape: background
            position: (0,0)
            size: 7x7
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Objects:** Three azure (color 8) objects that are approximately L-shaped are present.

2.  **Locate Change:**  Blue pixels are inserted into each of the L-shaped objects. The locations are different.

3.  **Transformation Rule:**
    *   Preserve the azure (color 8) L-shaped objects in their original positions.
    *   Change the color of one pixel of each object from azure (8) to blue (1):
        * The right-most pixel of the first object.
        * The bottom-most pixel for the second object.
        * The top-most pixel of the third object.

**Natural Language Program**

Here's the program in natural language:

1.  Copy the input grid to the output grid.
2.  Identify the approximately L-shaped azure objects.
3.  For the first L-shaped object, change the color of its right-most pixel to blue (1).
4.  For the second L-shaped object, change the color of its bottom-most pixel to blue (1).
5.  For the third L-shaped object, change the color of its top-most pixel to blue (1).

```python
"""
Copies the input grid to the output grid, then finds three specific L-shaped azure objects and modifies them.
"""

import numpy as np

def find_l_shapes(grid, color):
    # helper function for finding objects (same as before)
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if not is_valid(x, y) or visited[x, y] or grid[x, y] != color:
            return

        visited[x, y] = True
        current_object.append((x, y))

        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and not visited[x, y]:
                current_object = []
                dfs(x, y, current_object)
                # check for approximate shape and size
                if 3 <= len(current_object) <= 5:
                    objects.append(current_object)

    return objects

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    if len(l_shapes) >= 3:
        # Process the first L-shape (right-most)
        first_l_shape = l_shapes[0]
        rightmost_pixel = max(first_l_shape, key=lambda p: p[1])
        output_grid[rightmost_pixel] = 1

        # Process the second L-shape (bottom-most)
        second_l_shape = l_shapes[1]
        bottommost_pixel = max(second_l_shape, key=lambda p: p[0])
        output_grid[bottommost_pixel] = 1

        # Process the third L-shape (top-most)
        third_l_shape = l_shapes[2]
        topmost_pixel = min(third_l_shape, key=lambda p: p[0])  # Use min for top-most
        output_grid[topmost_pixel] = 1


    return output_grid
```

The code uses the same object finding logic. The main difference is the addition of the `topmost_pixel` logic, and ensuring there are at least three L-shaped objects before attempting to modify the third one. The `min` function is used, as smaller row indices are closer to the top of the grid.

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
