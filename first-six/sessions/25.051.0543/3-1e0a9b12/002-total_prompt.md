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

Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  dimensions: 4x4
  objects:
    - color: 4 (yellow)
      positions: [(0, 1), (2, 1)]
    - color: 9 (maroon)
      positions: [(0, 3)]
    - color: 6 (magenta)
      positions: [(2, 2)]
    - color: 1 (blue)
      positions: [(3, 0)]
  background_color: 0 (white)

output_grid:
  dimensions: 4x4
  objects:
    - color: 4 (yellow)
      positions: [(2,1), (3, 1)]
    - color: 9 (maroon)
      positions: [(3, 3)]
    - color: 6 (magenta)
      positions: [(3, 2)]
    - color: 1 (blue)
      positions: [(3, 0)]
  background_color: 0 (white)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid contains four single-cell objects of colors 1 (blue), 4 (yellow), 6 (magenta), and 9 (maroon), and all other cells are 0 (white).

2.  **Move Objects:** The program proceeds as follow:
    - The yellow object at (0,1) moves to (2,1).
    - All the objects are moved to the last row of the grid, preserving their original column. In detail:
      - The object of color 1 (blue) moves from (3, 0) to (3, 0).
      - The object of color 4 (yellow) moves from (0, 1) to (3, 1).
      - The object of color 6 (magenta) moves from (2, 2) to (3, 2).
      - The object of color 9 (maroon) moves from (0, 3) to (3, 3).

3. **Final Output**: The other cells, not occupied by the moved objects, become or remain 0.

In summary, all the single colored cells move to the last row.
The cells that are not affected by the move become, or remain, 0.

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
