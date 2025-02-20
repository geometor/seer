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

**Observations and Documentation**

Here's a YAML block summarizing my initial findings:

```yaml
input_grid:
  size: 4x4
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
  size: 4x4
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

**Determining the Transformation Rule**

Here's my natural language description of the step-by-step transformation:

1.  **Identify Objects:** The input grid contains four single-cell objects of colors 1, 4, 6, and 9.

2.  **Move Objects:** Each object moves to the last row. The relative horizontal positions of objects remain in the same column.

3. **Move one object '4':** Object '4' which was originally present at cell (0,1) moved at position (2,1) in the final grid.

**Natural Language Program**
1. Find all objects of different colors.
2. Move objects in the last row, preserving its horizontal order.
3. Move one object '4' one row up.


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
