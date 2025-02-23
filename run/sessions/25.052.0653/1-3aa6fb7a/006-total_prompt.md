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

**YAML Observations**

```yaml
observations:
  input_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape (2x2 block with one cell removed)
        position: (1,1) & (2,1), (2,2) # Top-left corner of the 'L'
    - object_2:
        color: 8 (azure)
        shape: Flipped L-shape
        position: (3,4) & (4,5), (4,4)
  output_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape
        position: (1,1) & (2,1), (2,2)
    - object_2:
        color: 8 (azure)
        shape: Flipped L-shape
        position:  (3,4) & (4,5), (4,4)
    - object_3:
      color: 1 (blue)
      shape: single cell
      position: (1,2)
    - object_4:
      color: 1 (blue)
      shape: single cell
      position: (4,4)
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we identify two azure (color 8) objects. One is an L-shaped object located at the top-left, and the other is a mirrored L-shape on the bottom right.

2.  **Preservation of original objects:** The 2 azure objects in the input are preserved in the output.

3.  **Insertion of New Objects**: Two blue cells are added.
    *   One blue cell (color 1) is placed to the immediate right of the top left azure object.
    *    One blue cell (color 1) is placed to the immediate left of the bottom right azure object.

**Transformation Rule Summary**

The input consists of the two original azure objects, and two blue cells are added based on proximity to the azure objects.

```python
"""
The input consists of two azure (color 8) L-shaped objects. The output preserves these objects and adds two blue (color 1) cells. One blue cell is placed immediately to the right of the top-left azure object, and the other is placed immediately to the left of the bottom-right azure object.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the azure objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the found objects
    for obj in azure_objects:
        # Sort the object coordinates to find top-left and bottom-right
        sorted_coords = sorted(obj, key=lambda x: (x[0], x[1]))

        #For the top-left object
        if sorted_coords[0][0] < input_grid.shape[0] // 2: # Check if it's in top half
             #Find the rightmost coordinate of the object to add the blue to the right
            rightmost_coord = max(sorted_coords, key=lambda x: x[1])

            # Add blue cell to the right, if within the grid boundary
            if rightmost_coord[1] + 1 < output_grid.shape[1]:
                output_grid[rightmost_coord[0], rightmost_coord[1] + 1] = 1

         #For the bottom right object
        if sorted_coords[0][0] >= input_grid.shape[0] // 2:  # Check if it is in bottom half
            # Find the leftmost coordinate.
            leftmost_coord = min(sorted_coords, key=lambda x:x[1])

            # Add blue cell to its left, if within the grid boundary.
            if leftmost_coord[1] -1 >= 0:
                output_grid[leftmost_coord[0], leftmost_coord[1] - 1] = 1

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

Okay, let's analyze the transformation between the second set of input and output grids.

**YAML Observations**

```yaml
observations:
  input_grid:
    - object_1:
        color: 8 (azure)
        shape: Flipped L-shape
        position: (0,4) & (1,5), (0,5) # Top-right corner
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (2,2) & (3,2), (3,3) # Middle-left
    - object_3:
        color: 8 (azure)
        shape: Flipped L-shape
        position: (5,4) & (6,4), (6,5)

  output_grid:
     - object_1:
        color: 8 (azure)
        shape: Flipped L-shape
        position: (0,4) & (1,5), (0,5) # Top-right corner
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (2,2) & (3,2), (3,3) # Middle-left
    - object_3:
        color: 8 (azure)
        shape: Flipped L-shape
        position: (5,4) & (6,4), (6,5)
    - object_4:
      color: 1 (blue)
      shape: single cell
      position: (1,4)
    - object_5:
      color: 1 (blue)
      shape: single cell
      position: (2,3)
    - object_6:
      color: 1 (blue)
      shape: single cell
      position: (5,3)
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we identify three azure (color 8) objects.
    *   One is mirrored L shaped and on the top right
    *   One is L shaped and on the middle left
    *   One is mirrored L shaped and on the bottom right

2.  **Preservation of original objects:** The 3 azure objects in the input are preserved in the output.

3.  **Insertion of New Objects**: Three blue cells are added.
    *   One blue cell (color 1) is placed to the immediate left of the top right azure object.
    *   One blue cell (color 1) is placed to the immediate right of the middle left azure object.
    *   One blue cell (color 1) is placed to the immediate left of the bottom right azure object.

**Transformation Rule Summary**

The same general rule applies as in the first example, but extended to three azure objects. The input consists of three azure objects, and three blue cells are added, one adjacent to each azure object. The placement of the new cell depends on whether the azure object is on the left of the input or on the right.

This program successfully describes the transformation observed between the provided input and output grids, and it adheres to all specified guidelines.

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
