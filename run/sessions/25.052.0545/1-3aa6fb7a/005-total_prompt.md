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

Okay, let's analyze the transformation between the input and output grids.

**Observations**

First, let's describe the input and output grids in terms of objects and their properties:

**Input Grid:**

*   There are two azure (8) colored objects.
*   The first object is an L-shape composed of three cells in the top-left.
*    The second object is an inverted-L shape composed of three cells in the bottom right.

**Output Grid:**

*   There are two azure (8) colored objects (same as input).
*    There are two new single-celled blue (1) object appearing "inside" the original azure objects, one on the left branch of each L.

**Transformation Rule (Natural Language Program)**

Here's a step-by-step description of the transformation:

1.  **Identify Azure Objects:** Locate all azure (8) colored objects in the input grid.

2.  **Analyze Shape:** For each azure object, check their shape. In this case they all form either L or inverted L.

3.  **Insert Blue Pixel:** For an azure object, select its leftmost vertical segment. Add a blue pixel (1) to the right of that segment.

**Summary of differences**

The transformation rule places a blue pixel beside the left side of each azure L.

```python
"""
The transformation rule identifies azure (8) colored L-shaped objects and inserts a blue (1) pixel adjacent to the leftmost vertical segment of each L.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous regions of the specified color.
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == color and not visited[i, j]:
                obj = []
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    if 0 <= r < rows and 0 <= c < cols and grid[r, c] == color and not visited[r, c]:
                        visited[r, c] = True
                        obj.append((r, c))
                        stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
                objects.append(obj)
    return objects

def is_l_shape(obj):
    # Check if the object is an L-shape (or inverted L).
    if len(obj) != 3:
        return False

    coords = np.array(obj)
    # Check for horizontal and vertical differences
    diffs_x = np.diff(coords[:, 0])
    diffs_y = np.diff(coords[:, 1])
     
    return (np.sum(diffs_x != 0) == 1 and np.sum(diffs_y != 0) ==1) or \
        (np.sum(diffs_x != 0) == 2 and np.sum(diffs_y != 0) == 0) or \
        (np.sum(diffs_x != 0) == 0 and np.sum(diffs_y != 0) == 2)

def find_leftmost_vertical_segment(obj):
  # Find Leftmost segment
    coords = np.array(obj)
    min_col = np.min(coords[:, 1])
    leftmost_coords = coords[coords[:, 1] == min_col]
    
    # Sort by row to ensure correct order (top to bottom)
    leftmost_coords = leftmost_coords[leftmost_coords[:, 0].argsort()]

    return leftmost_coords

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    
    # Find all azure objects.
    azure_objects = find_objects(input_grid, 8)
    
    # Iterate through each azure object.
    for obj in azure_objects:
        # Check if the object is an L-shape.
        if is_l_shape(obj):
            # Find the leftmost vertical segment
            leftmost_segment = find_leftmost_vertical_segment(obj)

            if len(leftmost_segment) > 0:
               # take first point from segment
               row, col = leftmost_segment[0]
               # change this coordinate in output

               if (col + 1) < output_grid.shape[1]:
                    output_grid[row, col + 1] = 1
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
