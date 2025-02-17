# 1-3aa6fb7a • 002 • example_1 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F6FBC416EF0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F6FBC417DF0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
input_grid:
  objects:
    - color: 8
      shape: two separate 2x1 vertical and 1x2 horizontal rectangles
      position: (1,1) and (3,4) # Starting row and column indices for the top-left corner of each rectangle
    - color: 0
      shape: background
      position: fills the rest of the grid

output_grid:
  objects:
    - color: 8
      shape: two separate 2x1 vertical and 1x2 horizontal rectangles.
      position:  (1,1) and (3,4)  #Same position
    - color: 1
      shape: single cell
      position: (1,2) and (4,5) #fills the spaces
    - color: 0
      shape: background
      position: fills the rest of the grid
```

**Natural Language Program**

Here's a step-by-step description of the observed transformation:
1.  **Identify Objects:** In the input grid, we have the following objects: two azure (color 8) colored rectangles, and the background (color 0).
2.  **Azure Rectangles Properties:** Two azure rectangles, are not modified. One is located in column 1 and rows 1 and 2, and consists in two azure cells vertically. The other is located in row 4 and columns 4 and 5, and consists in two horizontally placed azure cells.
3.  **Change**: The cells that:
    +   have a direct neighbor to the left of color 8.
    +   have a direct neighbor to the right of color 8.

    are changed to the color blue (1).

**Transformation Rule**
The transformation rule can be described as background. For each cell, If a cell, that is not part of a azure rectangle, is between two azure colored cells (neighbor to the left is azure and neighbor to the right is azure), change the cells to blue (1).


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
