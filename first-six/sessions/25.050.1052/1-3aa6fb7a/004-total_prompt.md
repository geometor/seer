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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74DAABC42020>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74DAABC42860>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape
      position: (1,1)  # Top-left corner of the object
      size: 3
    - color: 8 (azure)
      shape: L-shape
      position: (3,4)  # Top-left corner of the object
      size: 3
  background:
    - color: 0 (white)

output_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape
      position: (1,1)  # Top-left corner of the object
      size: 3
    - color: 1 (blue)
        shape: single cell
        position: (1,2)
        size: 1
    - color: 8 (azure)
      shape: L-shape
      position: (3,4) # Top-left corner of the object
      size: 3
    - color: 1 (blue)
        shape: single cell
        position: (4,5)
        size: 1
  background:
    - color: 0 (white)

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can identify two azure (color 8) L-shaped objects of size 3. And the background is composed by white cells (color 0).

2.  **Detect the change**
    *   Locate the uppermost and leftmost azure cell of the first azure L-shape.
    *   Change the color of the cell to the immediate right to blue (color 1)

    *   Locate the uppermost and leftmost azure cell of the second azure L-shape.
    *   Change the color of the cell to the immediate down to blue (color 1).

**Transformation Rule Summary**

The transformation rule can be summarized as:
*For each azure L-shape object in the input grid, paint in blue (color 1) the right/down neighbor cell of its upper left pixel.*

```python
"""
For each azure L-shape object in the input grid, paint in blue (color 1) the right/down neighbor cell of its upper left pixel.
"""

import numpy as np

def find_l_shapes(grid, color):
    # Find all L-shaped objects of a specific color in the grid.
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L-shape (3 cells)
                if grid[r + 1, c] == color and grid[r, c + 1] == color :
                    l_shapes.append((r, c))
                elif grid[r+1,c] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))
                elif grid[r,c+1] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each azure L-shape object, change the color of the cell to the immediate right
    of its top-left corner to blue.
    """
    output_grid = np.copy(input_grid)
    azure_l_shapes = find_l_shapes(output_grid, 8)

    for r, c in azure_l_shapes:
        #Check the shape of each L
        if output_grid[r + 1, c] == 8 and output_grid[r, c + 1] == 8 :
           # Change the cell to the right of the top-left corner to blue
           if c + 1 < output_grid.shape[1]:
              output_grid[r, c + 1] = 1
        elif output_grid[r+1,c] == 8 and output_grid[r+1,c+1] == 8:
             if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c] = 1
        elif output_grid[r,c+1] == 8 and output_grid[r+1,c+1] == 8:
            if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c+1] = 1
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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74DAABC20550>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74DAABC205E0>
Okay, let's analyze the second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape
      position: (0,4)  # Top-left corner
      size: 3
    - color: 8 (azure)
      shape: L-shape
      position: (2,2) # Top-left corner
      size: 3
        - color: 8 (azure)
      shape: L-shape
      position: (5,3)  # Top-left corner
      size: 3
  background:
    - color: 0 (white)

output_grid:
 objects:
    - color: 8 (azure)
      shape: L-shape
      position: (0,4)  # Top-left corner
      size: 3
    - color: 1 (blue)
      shape: single cell
      position: (1,4)  # Top-left corner
      size: 1
    - color: 8 (azure)
      shape: L-shape
      position: (2,2) # Top-left corner
      size: 3
    - color: 1 (blue)
      shape: single cell
      position: (2,3)  # Top-left corner
      size: 1
    - color: 8 (azure)
      shape: L-shape
      position: (5,3)  # Top-left corner
      size: 3
    - color: 1 (blue)
      shape: single cell
      position: (5,3)  # Top-left corner
      size: 1

  background:
    - color: 0 (white)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid contains three azure (color 8) L-shaped objects and white cells (color 0) that compose the background.

2.  **Transformation Rule:**
    *   Locate the azure (color 8) L-shaped objects.

     *   Locate the uppermost and leftmost azure cell of the first azure L-shape.
    *   Change the color of the cell to the immediate down to blue (color 1)

     *   Locate the uppermost and leftmost azure cell of the second azure L-shape.
    *   Change the color of the cell to the immediate right to blue (color 1).

    *   Locate the uppermost and leftmost azure cell of the third azure L-shape.
    *   Change the color of the cell to the immediate left to blue (color 1).

**Transformation Rule Summary**

The transformation rule is:

*For each azure L-shape in the input grid:*
*Find its uppermost and leftmost cell. Check the shape to determine if we should paint the cell down, right or up of the top-left corner.*
*If the shape is vertical paint in blue (color 1) down.*
*If the shape is horizontal paint in blue (color 1) right.*

It appears that there is an error in my code. I missed the third L-shape in the second example because I considered only two types of L shapes.
Here is the modified function :

```python
"""
For each azure L-shape in the input grid:
Find its uppermost and leftmost cell. Check the shape to determine if we should paint the cell down, right or up of the top-left corner.
If the shape is vertical paint in blue (color 1) down.
If the shape is horizontal paint in blue (color 1) right.
"""

import numpy as np

def find_l_shapes(grid, color):
    # Find all L-shaped objects of a specific color in the grid.
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L-shape (3 cells)
                if grid[r + 1, c] == color and grid[r, c + 1] == color :
                    l_shapes.append((r, c))
                elif grid[r+1,c] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))
                elif grid[r,c+1] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each azure L-shape object, change the color of the cell to the immediate right
    of its top-left corner to blue.
    """
    output_grid = np.copy(input_grid)
    azure_l_shapes = find_l_shapes(output_grid, 8)

    for r, c in azure_l_shapes:
        #Check the shape of each L
        if output_grid[r + 1, c] == 8 and output_grid[r, c + 1] == 8 :
           # Change the cell to the right of the top-left corner to blue
           if c + 1 < output_grid.shape[1]:
              output_grid[r, c + 1] = 1
        elif output_grid[r+1,c] == 8 and output_grid[r+1,c+1] == color:
             if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c] = 1
        elif output_grid[r,c+1] == 8 and output_grid[r+1,c+1] == 8:
            if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c+1] = 1
    return output_grid
```

I made a mistake in my previous code, because, I was using `output_grid[r + 1, c + 1] = 1` to paint, when the correct position is given by `output_grid[r, c -1]`. I think now all edge cases will be handled by the function. Here is the corrected Python Code.

```python
"""
For each azure L-shape in the input grid:
Find its uppermost and leftmost cell. Check the shape to determine if we should paint the cell down, right or up of the top-left corner.
If the shape is vertical paint in blue (color 1) down.
If the shape is horizontal paint in blue (color 1) right.
"""

import numpy as np

def find_l_shapes(grid, color):
    # Find all L-shaped objects of a specific color in the grid.
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L-shape (3 cells)
                if grid[r + 1, c] == color and grid[r, c + 1] == color :
                    l_shapes.append((r, c))
                elif grid[r+1,c] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))
                elif grid[r,c+1] == color and grid[r+1,c+1] == color:
                    l_shapes.append((r,c))
                elif grid[r,c-1] == color and grid[r+1,c-1] == color:
                    l_shapes.append((r,c))


    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    For each azure L-shape object, change the color of the cell to the immediate right
    of its top-left corner to blue.
    """
    output_grid = np.copy(input_grid)
    azure_l_shapes = find_l_shapes(output_grid, 8)

    for r, c in azure_l_shapes:
        #Check the shape of each L
        if output_grid[r + 1, c] == 8 and output_grid[r, c + 1] == 8 :
           # Change the cell to the right of the top-left corner to blue
           if c + 1 < output_grid.shape[1]:
              output_grid[r, c + 1] = 1
        elif output_grid[r+1,c] == 8 and output_grid[r+1,c+1] == 8:
             if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c] = 1
        elif output_grid[r,c+1] == 8 and output_grid[r+1,c+1] == 8:
            if r + 1 < output_grid.shape[0]:
                output_grid[r+1, c] = 1
        elif  output_grid[r,c-1] == 8 and output_grid[r+1,c-1] == 8:
           if c - 1 < output_grid.shape[1] and c > 0:
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
