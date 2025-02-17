# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7AB4D7BF9780>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7AB4D7BFAEC0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**Observations and Documentation**

Here's a YAML representation summarizing the initial observations:

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      shape: background
    - color: 4 (yellow)
      count: 2
      positions: [(0, 1), (2, 1)]
    - color: 9 (maroon)
      count: 1
      positions: [(0, 3)]
    - color: 6 (magenta)
      count: 1
      positions: [(2, 2)]
    - color: 1 (blue)
      count: 1
      positions: [(3, 0)]

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 11
      shape: background
    - color: 4 (yellow)
      count: 1
      positions:  [(2,1)]
    - color: 1 (blue)
      count: 1
      positions: [(3, 0)]
    - color: 6 (magenta)
      count: 1
      positions: [(3, 2)]
    - color: 9 (maroon)
      count: 1
      positions: [(3, 3)]
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Non-Zero Objects:** Locate all the cells in the input grid that have a non-zero color.

2.  **Move to Bottom Row:** Move all non-zero colored cells to the last (bottom) row of the output grid.

3.  **Maintain relative order.** Ensure that during the move, relative horizontal position is kept.

4. **Shift Yellow object on third row**: There is one yellow object that stays in the same position, the one in the third row.

**Natural Language Program**
1. Copy the input grid to the output grid.
2. Move all non-zero color objects to the last row, maintaining their relative horizontal order, except for the objects in the third row.
3. Make all objects in the first, second and last row and zero.


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
