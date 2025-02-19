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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76C86CF23EB0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76C86CF23460>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (1,1) # Top-left cell of the object
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (3,4) # Top-left cell of the object
  background:
    color: 0 (white)

output_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (1,1)
    - color: 1 (blue)
      shape: single cell
      position: (1,2)
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (3,4)
     - color: 1 (blue)
      shape: single cell
      position: (4,5)
  background:
    color: 0 (white)

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can identify two distinct L-shaped objects of color 8 (azure).

2.  **Detect Change:** One cell of color 1 (blue) has been added, connected to the top right side, to each of the L-shaped object of the input.

3. **Transformation Rule:** It fills with color 1 the cell at north-east position, considering the most western cell of each azure shape.

```python
"""
Transformation Rule: For each azure (color 8) L-shaped object in the input grid, a blue (color 1) cell is added to their north-east, considering the most western cell of each azure shape.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates (top-left cell) of each object.
    For simplicity, this function identifies each isolated groups of cells
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return []
        visited.add((r, c))
        cluster = [(r, c)]
        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                cluster.extend(dfs(r + dr, c + dc))
        return cluster

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                cluster = dfs(r, c)
                #find most western cell
                most_western_cell = cluster[0]
                for cell in cluster:
                    if cell[1] < most_western_cell[1]:
                        most_western_cell = cell
                objects.append(most_western_cell)

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each azure (color 8) L-shaped object, a blue (color 1) cell is added
    to their north-east, considering the most western cell of each azure shape.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Add a blue cell to the specified position relative to each azure object
    for r, c in azure_objects:
        new_r, new_c = r,c+1
        if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]:
          output_grid[new_r, new_c] = 1
        

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76C86CF224D0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76C86CF23490>
Okay, let's analyze the transformation between the input and output grids in this second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (0,4) # Top-left cell of the object
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (2,2) # Top-left cell of the object
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (5,3)
  background:
    color: 0 (white)

output_grid:
 objects:
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (0,4) # Top-left cell of the object
    - color: 1 (blue)
      shape: single cell
      position: (1,4)
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (2,2) # Top-left cell of the object
    - color: 1 (blue)
      shape: single cell
      position: (2,3)
       - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (5,3)
    - color: 1 (blue)
      shape: single cell
      position: (5,3)
  background:
    color: 0 (white)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can identify three distinct L-shaped objects of color 8 (azure).

2.  **Detect Change:** One cell of color 1 (blue) has been added. The position is connected to the top right side, to each of the L-shaped object of the input.

3. **Transformation Rule:** It fills with color 1 the cell at north-east position, considering the most western cell of each azure shape.

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
