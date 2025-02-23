# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7A151BB0F5E0>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7A151BB0DEA0>
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations in YAML format:**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      positions: [[0,0], [0,2], [1,0], [1,1], [1,2], [1,3], [2,0], [2,3], [3,1], [3,2]]
    - color: 4 (yellow)
      count: 2
      positions: [[0,1], [2,1]]
    - color: 9 (maroon)
      count: 1
      positions: [[0,3]]
    - color: 6 (magenta)
      count: 1
      positions: [[2,2]]
    - color: 1 (blue)
      count: 1
      positions: [[3,0]]

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 11
      positions: [[0,0], [0,1], [0,2], [0,3], [1,0], [1,1], [1,2], [1,3], [2,0], [2,2],[2,3]]
    - color: 4 (yellow)
      count: 2
      positions: [[3,1], [2,1]]
    - color: 9 (maroon)
      count: 1
      positions: [[3,3]]
    - color: 6 (magenta)
      count: 1
      positions: [[3,2]]
    - color: 1 (blue)
      count: 1
      positions: [[3,0]]
```

**Natural Language Program (Transformation Rule):**

1.  **Identify non-zero colored objects:** Locate all cells in the input grid that have a color other than 0 (white).
2.  **Move Identified objects:** Move the non-zero cells to the last row of the grid.
3.  **Preserve the bottom-up and left-right relative order**: When multiple non-zero colored objects are in a column they appear in the output following a bottom-up order and in case of objects in the same row they appear in the left to right order.

In summary, the transformation involves shifting all non-zero colored cells to the last row, while maintaining the bottom-up order for objects in the same column and preserving the left-right order for objects that were in the same row. The rest of the grid is filled with zeros.

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
