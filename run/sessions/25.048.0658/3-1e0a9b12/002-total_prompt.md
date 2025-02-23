# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x720C51F12320>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x720C51F12D40>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      shape: background
    - color: 4 (yellow)
      count: 2
      positions: (0,1), (2,1)
    - color: 9 (maroon)
      count: 1
      position: (0,3)
    - color: 6 (magenta)
      count: 1
      position: (2,2)
    - color: 1 (blue)
      count: 1
      position: (3,0)

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 11
      shape: background
    - color: 4 (yellow)
      count: 2
      shape: L-shape
      positions: (3, 1) (2,1)
    - color: 9 (maroon)
      count: 1
      position: (3,3)
    - color: 6 (magenta)
      count: 1
      position: (3,2)
    - color: 1 (blue)
      count: 1
      position: (3,0)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Non-Background Objects:** Locate all the colored cells (non-zero values) within the input grid.

2.  **Move Objects:** Move all identified non-background objects to the last row of the grid.

3. **Preserve Order:** Maintain the horizontal order of the objects as they appear from left to right in their original positions in the input.

**Natural Language Program**
```
Collect all non-background colored cells.
Move all of them to the last row.
Preserve the relative order of appearance from left to right.
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
