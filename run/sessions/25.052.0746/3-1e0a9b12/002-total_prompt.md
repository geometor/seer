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

**YAML Block Observation**

```yaml
observations:
  input_grid:
    size: 4x4
    objects:
      - color: 0 (white)
        count: 11
        shape: background
      - color: 4 (yellow)
        count: 2
        shape: isolated cells
        positions: [0,1], [2,1]
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [0,3]
      - color: 6 (magenta)
        count: 1
        shape: isolated cell
        position: [2,2]
      - color: 1 (blue)
        count: 1
        shape: isolated cell
        position: [3,0]

  output_grid:
    size: 4x4
    objects:
      - color: 0 (white)
        count: 12
        shape: background
      - color: 4 (yellow)
        count: 1
        shape: isolated cell
        position: [2,1]
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [3,3]
      - color: 6 (magenta)
        count: 1
        shape: isolated cell
        position: [3,2]
      - color: 1 (blue)
        count: 1
        shape: isolated cell
        position: [3,0]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of isolated cells of colors 1 (blue), 4 (yellow), 6 (magenta), and 9 (maroon) against a background of color 0 (white).

2.  **Predicate:** The non-white cells maintain their colors.

3. **Action:** Move the colored cells to the bottom row, maintaining the x value, stacking the cells in order from bottom to top, keeping the original colors.

**Transformation Rule Summary**
The transformation moves all non-zero colored cells to the last row available, keeping their original colors. The colored objects do not change color, they are just translated.

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
