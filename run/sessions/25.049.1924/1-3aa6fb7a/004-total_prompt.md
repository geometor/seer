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

<PIL.Image.Image image mode=RGB size=448x448 at 0x705FD090E320>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x705FD090EA10>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate L-shapes, one mirrored"
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate L-shapes, one mirrored"
     - color: 1
       positions: [(4,4), (1,2)]
```

**Natural Language Description of the Transformation**

1.  **Identify Objects:** In the input grid, we can identify two distinct objects of color `8` (azure). One object at the top left, is composed by cells (1,1), (2,1) and (2,2). The other one, at the bottom right, is composed by cells (3,4), (3,5) and (4,5).

2.  **Detect Changes:** The azure objects remain unchanged between the input and output. In the output we can observe two new blue pixels (color code 1).

3.  **Describe New Objects:**
 *    The first new pixel in the output is at the position (1,2) of the original top-left shape.
 *    The second new pixel in the output is at the position (4,4) the original bottom-right shape.

4. **Transformation rule**: For each azure object, compute the centroid and change the value of this cell to `1` (blue).

**Step-by-step transformation**
1. Find each isolated azure object.
2. For each of them: Paint with blue the cell corresponding to their centroid.

```python
"""
Transformation Rule:

1.  **Identify Objects:** Find all distinct azure (color code 8) objects in the input grid.
2.  **Calculate Centroids:** For each identified azure object, calculate its centroid.
3.  **Paint Centroids:** Change the color of the cells corresponding to the calculated centroids to blue (color code 1).
"""

import numpy as np
from scipy.ndimage import measurements

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of coordinates for each object found.
    """
    mask = (grid == color).astype(int)
    labeled_array, num_features = measurements.label(mask)
    objects = []
    for i in range(1, num_features + 1):
        coords = np.array(np.where(labeled_array == i)).T
        objects.append(coords)
    return objects

def calculate_centroid(coords):
    """
    Calculates the centroid of a set of coordinates.
    """
    return np.mean(coords, axis=0).astype(int)

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = input_grid.copy()

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    # Calculate the centroid for each azure object and paint it blue
    for obj_coords in azure_objects:
        centroid = calculate_centroid(obj_coords)
        output_grid[centroid[0], centroid[1]] = 1  # Paint the centroid blue

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x705FD090EA70>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x705FD090EF50>
Okay, let's analyze the second example of transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three separate azure objects"
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 4), (6, 3)]
      shape: "Three separate azure objects"
    - color: 1
      positions: [(1, 4), (2, 3), (5,3)]
      shape: "three isolated pixels"
```

**Natural Language Description of the Transformation**

1.  **Identify Objects:** In the input grid, we can identify three distinct objects of color `8` (azure). One L-shaped object at the top right, composed by cells (0,4), (0,5) and (1,5). A second L-Shaped object in the center-left composed by cells (2,2), (3,2) and (3,3). The last one at the bottom, composed by cells (5,4), (6,3) and (6,4).

2.  **Detect Changes:** The azure objects remain unchanged between the input and output. In the output we can observe three new blue pixels (color code 1).

3.  **Describe New Objects:**
 *    The first new pixel in the output is at the position (1,4) of the original top-right shape centroid.
 *    The second new pixel in the output is at the position (2,3) the original center-left shape centroid.
 *    The third new pixel is at position (5,3) the original bottom shape centroid.

4. **Transformation rule**: For each azure object, compute the centroid and change the value of this cell to `1` (blue).

**Step-by-step transformation**
1. Find each isolated azure object.
2. For each of them: Paint with blue the cell corresponding to their centroid.

The transformation rule and the python program stay the same.
```python
"""
Transformation Rule:

1.  **Identify Objects:** Find all distinct azure (color code 8) objects in the input grid.
2.  **Calculate Centroids:** For each identified azure object, calculate its centroid.
3.  **Paint Centroids:** Change the color of the cells corresponding to the calculated centroids to blue (color code 1).
"""

import numpy as np
from scipy.ndimage import measurements

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of coordinates for each object found.
    """
    mask = (grid == color).astype(int)
    labeled_array, num_features = measurements.label(mask)
    objects = []
    for i in range(1, num_features + 1):
        coords = np.array(np.where(labeled_array == i)).T
        objects.append(coords)
    return objects

def calculate_centroid(coords):
    """
    Calculates the centroid of a set of coordinates.
    """
    return np.mean(coords, axis=0).astype(int)

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = input_grid.copy()

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    # Calculate the centroid for each azure object and paint it blue
    for obj_coords in azure_objects:
        centroid = calculate_centroid(obj_coords)
        output_grid[centroid[0], centroid[1]] = 1  # Paint the centroid blue

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
