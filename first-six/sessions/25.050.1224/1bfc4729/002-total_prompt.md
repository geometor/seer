# 1bfc4729 • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 6 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABAB79690>

**output**
```
6 6 6 6 6 6 6 6 6 6
6 0 0 0 0 0 0 0 0 6
6 6 6 6 6 6 6 6 6 6
6 0 0 0 0 0 0 0 0 6
6 0 0 0 0 0 0 0 0 6
7 0 0 0 0 0 0 0 0 7
7 0 0 0 0 0 0 0 0 7
7 7 7 7 7 7 7 7 7 7
7 0 0 0 0 0 0 0 0 7
7 7 7 7 7 7 7 7 7 7
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABB63AA10>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_objects:
  - color: 6 (magenta)
    position: (2, 2)
    shape: single cell
  - color: 7 (orange)
    position: (7, 7)
    shape: single cell
output_objects:
  - color: 6 (magenta)
    shape: 10x2 frame (top and bottom) and two 3x1 lines
  - color: 7 (orange)
      shape: 10x2 frame (top and bottom) and two 3x1 lines
```

**Natural Language Program: Step-by-step Transformation**

1.  **Identify Single Cells:** Locate all single-cell objects in the input grid. In this case, we find two: a magenta (6) cell at (2, 2) and an orange (7) cell at (7, 7).

2.  **Expand and frame based on color:**
    *   If the object is magenta (6), replicate it to top and bottom row. Then draw two lines, 3 cells down from the top, and 3 cells up from the bottom.
    *   If the object is orange (7), replicate it to top and bottom row. Then draw two lines, 3 cells down from the top, and 3 cells up from the bottom.

**Transformation Rule Summary**

The transformation rule involves taking each single-cell object in the input, and create frame and columns, depending on the original cell color.

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
