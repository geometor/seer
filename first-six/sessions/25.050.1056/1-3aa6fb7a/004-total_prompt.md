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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A151BB0F010>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A151BB0FE20>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate azure 'L' shapes, one in the top-left and other on the right"
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Same as input"
  - color: 1
    positions: [(4,1), (1,4)]
    shape: "Two, separate, individual blue cells."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. In this case, we have two distinct "L" shaped objects.

2.  **Preserve Azure Objects:** The azure objects are preserved from input to output.

3. **Detect top left corner and bottom right corner:** The upper-leftmost azure object is in position (1,1) and the bottom right most corner is (4,5).

4.  **Place blue pixels:** Place a blue (color 1) pixel on the corners of the bounding box of the object.

**Transformation Rule Summary**

The transformation rule is as follows:
- The azure colored objects are maintained from the input grid to the output grid.
- A blue pixel is placed in the grid at the top left corner and at the bottom right corner.

```python
"""
The azure colored objects are maintained from the input grid to the output grid.
A blue pixel is placed in the grid at the top left corner and at the bottom right corner of the azure colored cluster.
"""

import numpy as np

def find_azure_objects(grid):
    """
    Finds the positions of azure (color 8) pixels in the grid.
    """
    azure_positions = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 8:
                azure_positions.append((i, j))
    return azure_positions

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Azure objects are preserved.
    - Blue pixels are placed at the top-left and bottom-right corners of azure clusters.
    """
    output_grid = np.copy(input_grid)
    azure_positions = find_azure_objects(input_grid)

    if azure_positions:
      #find top-left and bottom-right corners
      min_row = min(pos[0] for pos in azure_positions)
      min_col = min(pos[1] for pos in azure_positions)
      max_row = max(pos[0] for pos in azure_positions)
      max_col = max(pos[1] for pos in azure_positions)

      output_grid[min_row, min_col] = 1 # top-left
      output_grid[max_row,max_col] = 1 # bottom-right

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A151BB0EB00>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A151BB0E9E0>
Okay, let's analyze the second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: "Scattered azure pixels forming three distinct clusters."
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: "Same as input"
    - color: 1
      positions: [(1, 4), (2,3), (5,3)]
      shape: "Three blue pixels."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. Here, three azure clusters of different shapes are visible.

2.  **Preserve Azure Objects:** The azure objects are preserved.

3. **Detect Azure object positions and put blue pixels:**
   For each azure colored object, find the "top-right" azure pixel within that object and move one pixel up and one pixel to the left to place a blue pixel (color 1).

**Transformation Rule Summary**

The transformation rule is as follows:

-   Azure objects are copied from the input to the output grid.
-   For each separate cluster of azure objects, find the top right most azure pixel within that cluster and transform the pixel up and to the left of that pixel to blue.

```python
import numpy as np

def find_azure_clusters(grid):
    """
    Finds separate clusters of azure (color 8) pixels.
    """
    visited = set()
    clusters = []

    def dfs(row, col, current_cluster):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != 8:
            return
        visited.add((row, col))
        current_cluster.append((row, col))
        # Check all 8 neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_cluster)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 8 and (i, j) not in visited:
                current_cluster = []
                dfs(i, j, current_cluster)
                clusters.append(current_cluster)
    return clusters

def transform(input_grid):

    output_grid = np.copy(input_grid)
    azure_clusters = find_azure_clusters(input_grid)

    for cluster in azure_clusters:
        if cluster:
            #Find top-right corner of each cluster
            top_right_row =  min(pos[0] for pos in cluster)
            possible_cols = [pos[1] for pos in cluster if pos[0] == top_right_row]
            top_right_col = max(possible_cols)

            # Place blue pixel one up and one left if possible.
            if(top_right_row-1 >= 0 and top_right_col-1 >= 0):
              output_grid[top_right_row - 1, top_right_col - 1] = 1

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
