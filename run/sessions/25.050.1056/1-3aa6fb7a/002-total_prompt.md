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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A151BB0F010>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A151BB0FE20>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate azure 'L' shapes, one in the top-left and other on the right"
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Same as input"
  - color: 1
    positions: [(4,1), (1,4)]
    shape: "Two, separate, individual blue cells."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. In this case, we have two distinct "L" shaped objects.

2.  **Preserve Azure Objects:** The azure objects are preserved from input to output.

3. **Detect top left corner and bottom right corner:** The upper-leftmost azure object is in position (1,1) and the bottom right most corner is (4,5).

4.  **Place blue pixels:** Place a blue (color 1) pixel on the corners of the bounding box of the object.

**Transformation Rule Summary**

The transformation rule is as follows:
- The azure colored objects are maintained from the input grid to the output grid.
- A blue pixel is placed in the grid at the top left corner and at the bottom right corner.

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
