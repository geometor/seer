# 6-0520fde7 • 002 • example_1 - CODE

---

**input**
```
1 0 0 5 0 1 0
0 1 0 5 1 1 1
1 0 0 5 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0
0 2 0
0 0 0
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Summary of Observations**

```yaml
task: 001
observations:
  input_grid:
    size: 3x7
    objects:
      - color: 1
        shape: irregular
        positions: [(0,0), (0,5), (1,1), (1,4), (1,5), (1,6), (2,0)]
      - color: 5
        shape: vertical line
        positions: [(0,3), (1,3), (2,3)]
      - color: 0
        shape: background
        positions: fills the rest
  output_grid:
    size: 3x3
    objects:
      - color: 2
        shape: single cell
        positions: [(1,1)]
      - color: 0
        shape: background
        positions: fills the rest
```

**Natural Language Program**

1.  **Identify Objects:** In the input grid, we observe three distinct types of objects based on color: objects of color 1 (blue), objects of color 5 (gray), and the background color 0 (white).

2.  **Focus Object:** The output grid is 3x3. The output grid is always the minimal size that includes all non-background colors.

3. **Color Mapping**
    The color 5 is transformed to color 2 (red). Other non-background colors are deleted.

4.  **Transformation Rule:** The output is a 3x3 grid. Non-background colors are removed, except color 5 that is mapped to color 2.

**In Summary**

The transformation rule involves creating a new 3x3 grid. In this new grid only color 5, mapped to color 2, is copied. Other colors are transformed to the background color.

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
