# 00d62c1b • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x79CABB63B640>

**output**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x79CABB63B520>
Okay, I'm ready to analyze the transformation between the input and output grids. Here's my breakdown:

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 3 (green)
      shape: Cross-like pattern
      positions: [(1, 2), (2, 1), (2, 3), (3, 2), (4, 3)]
    - color: 0 (white)
      shape: Background
      positions: All other cells

output_grid:
  objects:
    - color: 3 (green)
      shape: similar cross-like pattern, but 2 cells are different color
      positions: [(1, 2), (2, 1), (2, 3), (3, 2), (4, 3)]
    - color: 4 (yellow)
      shape: single cells inside the green object.
      positions: [(2,2), (3,3)]
    - color: 0 (white)
      shape: Background
      positions: All other cells
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify the Green Object:** Locate the contiguous "cross-like" shaped object formed by cells of color 3 (green) in the input grid.

2.  **Locate the center:** Inspect the cells that belong to the green object. Locate the cell that belongs to object 3, that is surrounded, on its top, bottom, left and right, by other cells that belong to the object, paint that yellow.

3. **Repeat:** Repeat the process for other cells of the object that meet similar conditions.

**Elaboration and Explanation**
The core transformation involves the object with color 3. Two cells from it are changing their colors.

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
