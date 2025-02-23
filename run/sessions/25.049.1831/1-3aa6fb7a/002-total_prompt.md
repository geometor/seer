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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A3068516260>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7A3068516A70>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Two separate 2x1 vertical and 1x2 horizonal rectangles.

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 4)]
      shape: Two separate 2x1 vertical and 1x2 horizonal rectangles.
    - color: 1 (blue)
      positions: [(1,2), (5,4)]
      shape: single pixels.
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Azure Objects:** In the input grid, we observe two distinct objects formed by azure (color 8) pixels. One is in the top-left corner consists in a vertical rectangle, and the other is in the center-right and forms an horizontal rectangle.

2.  **Locate Topmost and Leftmost**: For each of the azure objects, find the coordinate that has color 8.

3.  **Change to Blue**: The right adjacent cell to the leftmost azure pixel for the upper object is turned to blue (1), and the down adjacent cell for the leftmost azure pixel is changed to blue (1) for the lower object.

4. **Preserve**: The original azure objects are kept in the ouput.

In essence, the transformation identifies azure objects, and changes the next cell to its right or down, based on their location, to blue, leaving the remaining parts of the input grid unchanged.

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
