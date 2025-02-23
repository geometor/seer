# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79B96C7FA770>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79B96C7FB9D0>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations in YAML Format**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      positions: Most of the grid
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
      positions: Most of the grid
    - color: 4 (yellow)
      count: 1
      positions: (3,1)
    - color: 1 (blue)
      count: 1
      position: (3, 0)
    - color: 6 (magenta)
      count: 1
      position: (3, 2)
    - color: 9 (maroon)
      count: 1
      position: (3, 3)
```

**Natural Language Program Description**

Here's a step-by-step description of the transformation:

1.  **Identify non-white cells:** Locate all cells in the input grid that do *not* have the color white (0).

2.  **Move to Bottom Row, Preserve Order**: Move a copy of all the non-white cells to the last row of the grid. The order of non-white cells in the input is maintained in the output: The colored cells are arranged in the last row, sorted from left to right, following the column major order in the input.

3. **Remove**: Remove cells that have the same value of an adjacent cell (left, right, up, down).

**Inferred Transformation Rule Summary**

The transformation rule can be summarized as follows:
The colored objects from the input are copied and consolidated/moved into the bottom row of the output grid, maintaining their original order, and removing equal adjacent colored cells. The remaining cells are set to white (0).

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
