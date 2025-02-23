# 1-3aa6fb7a • 006 • example_2 - CODE

---
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

