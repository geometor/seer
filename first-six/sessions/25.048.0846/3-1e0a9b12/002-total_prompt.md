# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7017B29F90F0>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7017B29FB040>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations in YAML Format**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 4 (yellow)
      positions: [(0, 1), (2, 1)]
    - color: 9 (maroon)
      positions: [(0, 3)]
    - color: 6 (magenta)
      positions: [(2, 2)]
    - color: 1 (blue)
      positions: [(3, 0)]
    - color: 0 (white)
      positions: All other cells

output_grid:
  size: 4x4
  objects:
    - color: 4 (yellow)
      positions: [(2,1), (3, 1)]
    - color: 9 (maroon)
      positions: [(3, 3)]
    - color: 6 (magenta)
      positions: [(3, 2)]
    - color: 1 (blue)
      positions: [(3, 0)]
    - color: 0 (white)
      positions: All other cells
```

**Natural Language Program Description**

1.  **Identify Non-White Objects:** Locate all cells in the input grid that are not white (color 0).

2.  **Move Objects:** The non-white objects are moved/translated to the bottom row of the output grid.

3.    **Preserve Order:** Specifically, the non-white objects present maintain their relative horizontal order when moved.
    *   The leftmost non-white object in the input (blue, color 1) becomes the leftmost in the bottom row of the output.
    *   The second non-white object (yellow color 4) stays the second.
    *   The next yellow object is moved down.
    *   The magenta and maroon objects maintain their order as well.

4. **Clear other Cells.** All cells that are not part of the final positions of the copied objects are set to color 0.

In summary, the transformation involves moving all non-white cells to the last row, preserving their original horizontal order, and setting all other cells to white.

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
