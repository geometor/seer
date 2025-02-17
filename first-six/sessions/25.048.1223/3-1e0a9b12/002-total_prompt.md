# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7DEBC94F6AD0>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7DEBC94F5840>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

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

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all non-white colored cells in the input grid.

2.  **Shift Objects:**
    All the non-white colored pixels are moved to the last row, keeping it's order.

3. **Place Objects on the bottom:**
    *   The yellow object that was originally at (0, 1) is moved to (3,1)
    *   The yellow object that was originally at (2, 1) is moved to (3,1)
    *   The maroon object originally at (0, 3)is moved to (3, 3).
    *    The magenta object originally at (2,2) is moved to (3,2)
    *   The blue object at (3, 0) stays at (3, 0).

4. **All other cells:** fill all others cells with white (0)

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
