# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Observations**

```yaml
task: 001-example_1
observations:
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
  output_grid:
    size: 4x4
    objects:
      - color: 4 (yellow)
        positions: [(2, 1), (3,1)]
      - color: 9 (maroon)
        positions: [(3, 3)]
      - color: 6 (magenta)
        positions: [(3, 2)]
      - color: 1 (blue)
        positions: [(3, 0)]
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** Locate all colored cells (non-zero) in the input grid. The objects here are individual single colored cells.

2.  **Move Down:** Each colored object of the grid moves down.

3. **Bottom Row Priority:** If any colored cells are in the last row, they persist in their positions.

4.  **Stack:** If by moving down, two or more objects coincide, the object originally positioned lower takes the place.

**Transformation Rule Summary**

The transformation involves moving down all the colored cells to the bottom row.


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
