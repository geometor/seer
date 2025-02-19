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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7B047A219C60>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7B047A21AA10>

*text:*
**Natural Language Program:**

The task is to identify connected regions of color '8' in the input grid. For each such region, we need to determine a transformation based on its vertical position in the grid.

1. **Identify Connected Regions:** Find all groups of connected cells that have the color '8'. Connectivity is defined as being adjacent horizontally or vertically.
2. **Calculate Average Row Index for Each Region:** For each connected region, calculate the average row index of all cells belonging to that region.
3. **Determine Transformation Rule based on Average Row Index:**
    - Calculate a threshold row index as the integer division of the grid height by 2. In this case, grid height is 7, so the threshold is 7 // 2 = 3.
    - **If the average row index of a region is less than the threshold (3):**
        a. Find the topmost row that contains any cell of this region.
        b. Within this topmost row, find the cell with the smallest column index that belongs to the region. Let's call this cell the "top-leftmost" cell.
        c. Change the color of the cell immediately to the right of this "top-leftmost" cell to '1', provided that this neighbor is within the grid boundaries.
    - **Otherwise (if the average row index is greater than or equal to the threshold 3):**
        a. Find the bottommost row that contains any cell of this region.
        b. Within this bottommost row, find the cell with the largest column index that belongs to the region. Let's call this cell the "bottom-rightmost" cell.
        c. Change the color of the cell immediately to the left of this "bottom-rightmost" cell to '1', provided that this neighbor is within the grid boundaries.

This program describes how to transform the input grid into the output grid by identifying connected regions of color '8' and applying different transformation rules based on their vertical position within the grid.
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
