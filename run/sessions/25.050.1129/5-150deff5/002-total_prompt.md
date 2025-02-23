# 5-150deff5 • 002 • example_1 - CODE

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
