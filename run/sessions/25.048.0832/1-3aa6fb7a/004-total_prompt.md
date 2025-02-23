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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7B5DFCC1EE00>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7B5DFCC1E1A0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      shape: L-shape
      position: (1,1) and (2,1), (2,2)
    - color: 8
      shape: reverse L-shape
      position: (4,4) and (3,4), (3,5)
  background_color: 0

output_grid:
  objects:
    - color: 8
      shape: L-shape
      position: (1,1) and (2,1), (2,2)
    - color: 1
      shape: single cell
      position: (1,2)
    - color: 8
      shape: reverse L-shape
      position: (4,4) and (3,4), (3,5)
    - color: 1
      shape: single cell
      position: (4,5)

  background_color: 0
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can identify two azure (color 8) L-shaped objects. The rest of the grid is filled with the background color (0).

2.  **Detect Change:** Compare the input and output. The azure L-shaped objects remain unchanged. However, a single cell of color blue(1) appears next to the 'leg' of each L shape.

3.  **Describe the rule:** For each azure object, the cell to the right of the bottom-most pixel of the object that is not part of that azure object gets colored blue (color 1).

**Transformation Rule (In Natural Language)**

The transformation rule can be stated as follows:

For each azure (color 8) object, find its bottom-most, non-connected point. Change the adjacent right cell of this point to blue (color 1). If the right cell is already part of the azure object, or if the right cell is out of boundary, do nothing.


*text:*
```python
"""
The transformation rule can be stated as follows:

For each azure (color 8) object, find its bottom-most, non-connected point. Change the adjacent right cell of this point to blue (color 1). If the right cell is already part of the azure object, or if the right cell is out of boundary, do nothing.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(row, col):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != color:
            return []

        visited.add((row, col))
        object_pixels = [(row, col)]

        object_pixels.extend(dfs(row + 1, col))
        object_pixels.extend(dfs(row - 1, col))
        object_pixels.extend(dfs(row, col + 1))
        object_pixels.extend(dfs(row, col - 1))

        return object_pixels
    
    for r in range(grid.shape[0]):
      for c in range(grid.shape[1]):
        if grid[r,c] == color and (r,c) not in visited:
          objects.append(dfs(r,c))

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule described above.
    """
    output_grid = np.copy(input_grid)
    azure_objects = get_objects(input_grid, 8)

    for obj in azure_objects:
        # Find the bottom-most pixels
        bottom_most_y = max(y for x, y in obj)
        bottom_pixels = [(x, y) for x, y in obj if y == bottom_most_y]
        
        # Sort bottom pixels by x coordinate to check for connectivity
        bottom_pixels_sorted = sorted(bottom_pixels, key=lambda p: p[0])
        
        for pixel in bottom_pixels_sorted:
          x,y = pixel
          
          #consider only the rightmost pixels in connected components of bottom_pixels
          if (x+1,y) not in bottom_pixels_sorted:
            # color the cell to right in output, boundary check
            if x + 1 < output_grid.shape[0] and y+1 < output_grid.shape[1] and x+1 < input_grid.shape[0]:
                if (x + 1, y) not in obj: # Check for adjanceny to L
                    output_grid[x + 1, y] = 1
                    break

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7B5DFCC1EDA0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7B5DFCC1E770>

*text:*
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      shape: reverse L-shape
      position: (0,4), (0,5), (1,5)
    - color: 8
      shape: L-shape
      position: (2,2), (3,2), (3,3)
    - color: 8
      shape: L-shape
      position: (5,4), (6,4), (6,5)
  background_color: 0

output_grid:
  objects:
    - color: 8
      shape: reverse L-shape
      position: (0,4), (0,5), (1,5)
    - color: 1
      shape: single cell
      position: (1,4)
    - color: 8
      shape: L-shape
      position: (2,2), (3,2), (3,3)
    - color: 1
      shape: single cell
      position: (2,3)
    - color: 8
      shape: L-shape
      position: (5,4), (6,4), (6,5)
     - color: 1
       shape: single cell
       position: (5,3)
  background_color: 0
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid contains three azure (color 8) objects, two are L-shaped and one is a reverse L-shaped.

2.  **Detect Change:** Comparing the input and output grids, we see that the azure objects remain in the same positions.  A blue (color 1) cell appears adjacent to each azure object.

3.  **Describe the rule:** For each azure object, find the rightmost pixel of its lowest row. The cell immediately to the left of this pixel is changed to blue (color 1).

**Transformation Rule (In Natural Language)**
The transformation rule is very similar to the first task.

For each azure (color 8) object:
1. Locate the *lowest* row of the azure object.
2. Identify the *right-most* pixel on that row.
3. Color the cell to the *left* of this identified cell to blue (color 1).
4. If there is an azure object directly to the left, do nothing.

The provided python code can implement this rule with minor changes.

```python
"""
The transformation rule is very similar to the first task.

For each azure (color 8) object:
1. Locate the *lowest* row of the azure object.
2. Identify the *right-most* pixel on that row.
3. Color the cell to the *left* of this identified cell to blue (color 1).
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(row, col):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != color:
            return []

        visited.add((row, col))
        object_pixels = [(row, col)]

        object_pixels.extend(dfs(row + 1, col))
        object_pixels.extend(dfs(row - 1, col))
        object_pixels.extend(dfs(row, col + 1))
        object_pixels.extend(dfs(row, col - 1))

        return object_pixels
    
    for r in range(grid.shape[0]):
      for c in range(grid.shape[1]):
        if grid[r,c] == color and (r,c) not in visited:
          objects.append(dfs(r,c))

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule described above.
    """
    output_grid = np.copy(input_grid)
    azure_objects = get_objects(input_grid, 8)

    for obj in azure_objects:
        # Find the bottom-most pixels
        bottom_most_row = max(r for r, c in obj)
        bottom_pixels = [(r, c) for r, c in obj if r == bottom_most_row]

        # Find the right-most pixel in the bottom row
        rightmost_pixel = max(bottom_pixels, key=lambda p: p[1])

        # Color the cell to the left of the rightmost pixel blue, with boundary checks
        r, c = rightmost_pixel
        if c > 0:  # Check if there's a cell to the left
            output_grid[r, c - 1] = 1

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
