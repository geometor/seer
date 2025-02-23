# 5-150deff5 • 004 • example_2 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0 0 0 0
0 0 5 5 5 5 5 0 0 0 0
0 0 0 5 5 5 0 0 0 0 0
0 0 0 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 5 0 0 0
0 0 0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=704x576 at 0x79D1211F3B80>

**output**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 8 8 0 0 0 0 0 0 0
0 0 8 8 2 2 2 0 0 0 0
0 0 0 2 8 8 0 0 0 0 0
0 0 0 2 8 8 8 8 0 0 0
0 0 0 2 0 0 8 8 0 0 0
0 0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=704x576 at 0x79D1211F2080>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 5
      shape: irregular
      position: centered
      size: 15
    - color: 0
      shape: background
      position: fills the entire grid
      size: remaining cells
output_grid:
  objects:
    - color: 8
      shape: approximate copy of the input object with color 5
      position: approximately the same position
      size: approximately the same size.
    - color: 2
      shape: approximate negative of the input object with color 5
      position: inside the first color 8 object.
    - color: 0
      shape: background
      position: fills the entire grid
      size: remaining cells

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the Object:** Find the contiguous region of color '5' (gray) in the input grid. This is our primary object.

2.  **Substitution 1:** Change all the cells of color 5 by color 8.

3.  **Substitution 2:** Every cell with value 0 and inside the object 1 (that is, surrounded by color 8 objects) will turn into color 2.

**Explanation and Justification**
The transformation performs substitutions, changing color 5 to color 8 and some internal cells to color 2.

```python
"""
The transformation rule is as follows:
1. Identify the Object: Find the contiguous region of color '5' (gray) in the input grid. This is our primary object.
2. Substitution 1: Change all the cells of color 5 by color 8.
3. Substitution 2: Every cell with value 0 and inside the object 1 (that is, surrounded by color 8 objects) will turn into color 2.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of all cells with the specified color.
    coords = np.argwhere(grid == color)
    return coords

def is_inside(grid, coord, object_coords):
    x, y = coord
    
    if any(np.array_equal(coord,obj_coord) for obj_coord in object_coords):
       return False
        
    #check west
    west = False
    for i in range(0,x):
        if [i,y] in object_coords.tolist():
          west = True

    east = False
    for i in range(x,grid.shape[0]):
        if [i,y] in object_coords.tolist():
          east = True
          
    north = False
    for i in range(0,y):
        if [x,i] in object_coords.tolist():
          north = True

    south = False
    for i in range(y,grid.shape[1]):
        if [x,i] in object_coords.tolist():
          south = True
          
    return west and east and north and south

def transform(input_grid):
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Find the object with color 5.
    object_coords = find_object(input_grid, 5)

    # Change color 5 to color 8.
    for coord in object_coords:
        output_grid[coord[0], coord[1]] = 8

    # Find cells with color 0 inside the object and change them to 2.
    for x in range(output_grid.shape[0]):
        for y in range(output_grid.shape[1]):
            if output_grid[x, y] == 0:
              if is_inside(output_grid, [x,y], object_coords):
                output_grid[x, y] = 2

    return output_grid
```


**input**
```
0 0 0 0 0 0 0 0 0 0
0 5 5 5 5 5 5 0 0 0
0 5 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x79D121213070>

**output**
```
0 0 0 0 0 0 0 0 0 0
0 8 8 2 8 8 2 0 0 0
0 8 8 2 8 8 2 0 0 0
0 0 0 2 0 0 2 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x79D121213640>
Okay, let's analyze the transformation between the provided input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 5
      shape: irregular
      position: centered-left
      size: 13
    - color: 0
      shape: background
      position: fills the entire grid
      size: remaining cells
output_grid:
  objects:
    - color: 8
      shape: partial copy of color 5
      size: less than the input size
    - color: 2
      shape: partial negative of the input object with color 5
      position: inside the first color 8 object.
    - color: 0
      shape: background
      position: fills the entire grid
      size: remaining cells

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the Object:** Find the contiguous region of color '5' (gray) in the input grid. This is our primary object.

2.  **Substitution 1:** Every other cell of color 5 will be substituted by the color 8. Starting from coordinate [1,1].

3.  **Substitution 2:** Every cell with value 0 and inside the object 1 (that is, surrounded by color 5 objects) will turn into color 2.

**Explanation and Justification**
The transformation performs two substitutions. First, every other cell with color 5 is transformed into a cell with color 8. Second, some internal cells to object 5 with color 0 are converted into cells with color 2.

```python
"""
The transformation rule is as follows:
1. Identify the Object: Find the contiguous region of color '5' (gray) in the input grid. This is our primary object.
2. Substitution 1: Every other cell of color 5 will be substituted by the color 8. Starting from coordinate [1,1].
3. Substitution 2: Every cell with value 0 and inside the object 1 (that is, surrounded by color 5 objects) will turn into color 2.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of all cells with the specified color.
    coords = np.argwhere(grid == color)
    return coords

def is_inside(grid, coord, object_coords):
    x, y = coord
    
    if any(np.array_equal(coord,obj_coord) for obj_coord in object_coords):
       return False
        
    #check west
    west = False
    for i in range(0,x):
        if [i,y] in object_coords.tolist():
          west = True

    east = False
    for i in range(x,grid.shape[0]):
        if [i,y] in object_coords.tolist():
          east = True
          
    north = False
    for i in range(0,y):
        if [x,i] in object_coords.tolist():
          north = True

    south = False
    for i in range(y,grid.shape[1]):
        if [x,i] in object_coords.tolist():
          south = True
          
    return west and east and north and south

def transform(input_grid):
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Find the object with color 5.
    object_coords = find_object(input_grid, 5)

    # Change color 5 to color 8.
    count = 0
    for coord in object_coords:
        if count % 2 == 0:
          output_grid[coord[0], coord[1]] = 8
        count+=1

    # Find cells with color 0 inside the object and change them to 2.
    for x in range(output_grid.shape[0]):
        for y in range(output_grid.shape[1]):
            if output_grid[x, y] == 0:
              if is_inside(input_grid, [x,y], object_coords):
                output_grid[x, y] = 2

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
