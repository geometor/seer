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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC5F21A470>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC5F21B340>
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: Two separate 1x2 vertical and horizontal rectangles.
    - color: 0 (white)
      positions: All other cells.
      shape: Background

output_grid:
    objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: Two separate 1x2 vertical and horizontal rectangles.
    - color: 1 (blue)
      positions: [(1,2), (4,4)]
      shape: Two 1x1 squares.
    - color: 0 (white)
      positions: All other cells.
      shape: Background
```

**Natural Language Description of the Transformation Rule**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. In this case, there are two separate azure objects.

2.  **Change corner to blue**: If a corner piece of the object exists, change it to blue.

3.  **Preserve Other Azure Cells:** All other azure cells that are not corner cells remain unchanged.

4. **Preserve background**: All white cells remain unchanged.

**Natural Language Program**
```
1. Find all separate azure (color 8) objects.
2. Locate the corner cells of the identified regions.
3. For each corner cell, change its color to blue (color 1).
4. Keep all other cells, both other azure colored and all the background, the same color.
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
