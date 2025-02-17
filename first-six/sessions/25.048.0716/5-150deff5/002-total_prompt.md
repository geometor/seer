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

<PIL.Image.Image image mode=RGB size=704x576 at 0x7DFEBCA1AD70>

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

<PIL.Image.Image image mode=RGB size=704x576 at 0x7DFEBCA19E70>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 5
      shape: irregular
      position: centered, extends from row 2 to row 7
      notes: Forms a sort of mirrored, almost symmetrical shape.
  background:
    color: 0

output_grid:
  objects:
    - color: 8
      shape: irregular, similar to the grey object in the input
      position: mirrors the general shape and location of the color 5 object, but smaller.
    - color: 2
      shape: fills the space between the outline object and the object of color 8
      position: surrounds object of color 8
  background:
    color: 0

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the Object:** Locate the contiguous region of color 5 (grey) in the input grid. This is the primary object.

2.  **Create an Outline:** Transform the outer layer of the gray object of color 5 into color 8.

3. **Create an Inner Object:** Fill the rest of the cells of color 5 with color 2.

**Transformation Rule Summary**

The transformation involves finding the shape formed by color 5, replacing the outer layer with color 8, and replacing the rest with color 2.

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
