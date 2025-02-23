# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block: Observations**

```yaml
input_grid:
  dimensions: 4x4
  objects:
    - color: 4
      positions: [(0, 1), (2, 1)]
    - color: 9
      positions: [(0, 3)]
    - color: 6
      positions: [(2, 2)]
    - color: 1
      positions: [(3, 0)]
  background_color: 0

output_grid:
  dimensions: 4x4
  objects:
    - color: 4
      positions: [(2,1), (3, 1)]
    - color: 9
      positions: [(3, 3)]
    - color: 6
      positions: [(3, 2)]
    - color: 1
      positions: [(3, 0)]
  background_color: 0
```

**Natural Language Program: Transformation Rule**

1.  **Identify Objects:** The input grid contains four distinct objects, each represented by a single-colored cell: yellow (4), maroon (9), magenta (6), and blue (1).

2.  **Object's displacement**: All objects are moved to the bottom.

3. **Preserve relative position**: The objects maintain their relative positions to each other.

4.  **Background:** The background color (0) remains unchanged.

**Elaboration of the points:**

*   The objects keep the X position of each cell.

*   The last row is entirely occupied by the different colored single-cell objects.

**Summary**

The transformation rule involves moving every non-zero object down to the last available row of the grid, while retaining the horizontal order. All the objects from the first row drop down to the last row. The order of the colored objects from the last row of the input is preserved, and the zero-colored cells in the last row are the only ones to change.

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
