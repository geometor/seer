# 4-0d3d703e • 002 • example_1 - CODE

---

**input**
```
3 1 2
3 1 2
3 1 2
```

![Image](000-example_1_input.png)


**output**
```
4 5 6
4 5 6
4 5 6
```

![Image](000-example_1_output.png)

**Natural Language Program:**

The transformation rule is a direct color substitution.  Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically:

- Color 3 (green) is transformed to color 4 (yellow).
- Color 1 (blue) is transformed to color 5 (gray).
- Color 2 (red) is transformed to color 6 (magenta).

The positions and arrangement of the colors are preserved; only the color values themselves are changed. The dimensions of the grid remain the same.
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
