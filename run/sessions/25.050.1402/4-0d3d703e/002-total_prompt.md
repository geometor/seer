# 4-0d3d703e • 002 • example_1 - CODE

---

**input**
```
3 1 2
3 1 2
3 1 2
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x778677E1B2B0>

**output**
```
4 5 6
4 5 6
4 5 6
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x778677E19E10>
**Natural Language Program: Transformation Rule**

For each cell in the input grid, apply the following color transformations:

1. **Identify the color value** of the cell in the input grid.
2. **Apply the transformation rule:**
   - If the color value is 3 (green), change it to 4 (yellow).
   - If the color value is 1 (blue), change it to 5 (gray).
   - If the color value is 2 (red), change it to 6 (magenta).
3. **Place the transformed color value** in the corresponding cell of the output grid.
4. **Repeat steps 1-3** for all cells in the input grid to generate the complete output grid.

In essence, this task involves a direct color-to-color substitution based on a fixed mapping rule applied uniformly across the entire grid. Each instance of a specific color in the input is consistently replaced with another specific color in the output.
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
